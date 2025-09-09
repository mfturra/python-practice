import csv
import os
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import logging
from urllib.parse import urlparse, parse_qs
import subprocess
import threading

# load env vars
load_dotenv()

# needs to include testing for Chrome, Mozilla, Edge, and Safari
# skip test: @pytest.mark.skip

@pytest.fixture(scope="module")
# @pytest.mark.smoke
# use webdriver to execute Chrome file
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def start_locust(client_file, web_port):
    """
    Function starts Locust in a separate thread
    """
    locust_command = ["locust", "--config", client_file, "--web-port", str(web_port)]
    subprocess.run(locust_command) # run locust server


def extract_page_metrics(driver):     
    """Helper function to extract page generation metrics"""

    # Clear performance data
    driver.execute_script("performance.clearMarks(); performance.clearMeasures(); performance.clearResourceTimings();")

    metrics = driver.execute_script("""
    const performanceTiming = performance.timing;
    const fcp = performance.getEntriesByName('first-contentful-paint')[0].startTime;
    const tti = performance.timing.domContentLoadedEventEnd - performance.timing.navigationStart;
    const ttfb = performanceTiming.responseStart - performanceTiming.navigationStart;
    const loadEventTime = performanceTiming.loadEventEnd - performanceTiming.navigationStart;
    const dcl = performanceTiming.domContentLoadedEventEnd - performanceTiming.navigationStart;
                                
    return {
            fcp: fcp,
            tti: tti,
            ttfb: ttfb,
            loadEventTime: loadEventTime,
            dcl: dcl
        };
    """)

    return metrics

def save_metrics_to_csv(writer, stage_title, metrics):
    """Helper function to save metrics into CSV"""
    # Write stage row
    writer.writerow([f"{stage_title}"])

    # Write metrics as a row
    writer.writerow(['FCP (ms)', 'TTI (ms)', 'TTFB (ms)', 'LET (ms)', 'DCL (ms)'])
    writer.writerow([
        metrics['fcp'],
        metrics['tti'],
        metrics['ttfb'],
        metrics['loadEventTime'],
        metrics['dcl']]
        )
    writer.writerow([])


def log_metrics(driver, stage_title, csv_writer=None):
    """Helper function to log metrics to CSV"""
    metrics = extract_page_metrics(driver)
    print(f"\nMetrics after {stage_title}:")
    print(f"First Contentful Paint: {metrics['fcp']:.2f} ms")
    print(f"Time to Interactive: {metrics['tti']:.2f} ms")
    print(f"Time to First Byte: {metrics['ttfb']:.2f} ms")
    print(f"Load Event Time: {metrics['loadEventTime']:.2f} ms")
    print(f"DOMContentLoaded: {metrics['dcl']:.2f} ms")

    if csv_writer:
        save_metrics_to_csv(csv_writer, stage_title, metrics)


def test_account_login(driver):
    try: 
        domain = os.getenv('DOMAIN')
        test_user = os.getenv('TESTUSER')
        password = os.getenv('PASSWORD')

        # Load page with web driver
        driver.get(domain)
        time.sleep(2) # required for extracting web page performance metrics

        # Extract metrics from end-to-end testing workflow
        with open('performance_metrics.csv', mode='w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)

            driver.execute_script("performance.mark('start_stage')")
            # Log and save metrics from Okta OAuth page
            log_metrics(driver, "Okta OAuth Page Load Metrics", csv_writer)
            # duration = driver.execute_script("return performance.getEntriesByType('measure').find(m => m.name === 'stage_duration').duration;")
            # print(f"Stage duration: {duration} ms")

            # # Extract current URL
            # current_url = driver.current_url
            # print(f'\nCurrent URL: {current_url}\n')

            # parsed_url = urlparse(current_url)
            # query_params = parse_qs(parsed_url.query)
            # state_token = query_params.get('stateToken', [None])[0]
            # print(f'stateToken: {state_token}')

            driver.execute_script("console.log(performance.getEntries());")
            driver.execute_script("console.log(performance.timing);")

            # Log and save metrics from User Credentials OAuth page
            log_metrics(driver, "User Credentials OAuth Page Load Metrics", csv_writer)

            # Locate username input
            WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, 'input28'))
                )
            
            # Pass in credentials to username page
            driver.find_element(By.ID, "input28").send_keys(test_user)
            time.sleep(1)

            # Submit Username credentials
            driver.find_element(By.XPATH, "//input[@type='submit']").click()
            
            # Extract metrics from password page loading workflow
            log_metrics(driver, "Password OAuth Page Load Metrics", csv_writer)

            # Extract metrics from password page loading workflow
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, 'input53'))
            )
            driver.find_element(By.ID, "input53").send_keys(password)
            time.sleep(1)

            # evaluate form submission functionality
            driver.find_element(By.XPATH, "//input[@type='submit']").click()
            print("\nLogin complete.")

            # Extract metrics from Final Login submission workflow
            log_metrics(driver, "Loading Final Login OAuth page")

    except Exception as e:
        print(f'Error retrieving access token: {str(e)}')
    # logging.info(f'Current URL: {current_url}\n\n')


    # try:
    #     token_storage = driver.execute_script(
    #         "return window.localStorage.getItem('okta-token-storage');"
    #     )
    #     if token_storage:
    #         access_token = driver.execute_script(
    #             "return JSON.parse(arguments[0]).accessToken.accessToken;", token_storage
    #         )
    #         print(f'Access Token: {access_token}')
    #     else:
    #         print('Okta-token-storage not found in local storage.')

    # except Exception as e:
    #     logging.error(f'An error occurred: {str(e)}')
        
    
    

    # trigger for testing workflow
    testing = False
    if testing == True:
        # Successful login completed
        print("\nStarting Locust for load testing...\n")

        # Start Locust server in a separate thread
        locust_client_path = "./client.conf"
        locust_web_port = 8099
        threading.Thread(target=start_locust, args=(locust_client_path, locust_web_port), daemon=True).start()

        print(f"\nLocust server started at http://localhost:{locust_web_port}\n")
        
        # check for locustfile running to configure browser close
        
        time.sleep(65)
    
    time.sleep(3)

@pytest.mark.skip
def test_chat_interface(driver):
    try: 
        # Find and click Access chat button
        chat_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Access chat"))  # Correct syntax
        )
        chat_button.click()
        time.sleep(3)

        # Find and click Accept button
        accept_terms_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "btn-secondary"))
        )
        accept_terms_button.click()
        time.sleep(3)

        # Find Chat box and input text
        chat_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "textarea"))
        )
        chat_box.send_keys("Summarize LLMs in two sentences at an 8th grade reading level.")
        time.sleep(3)

        # submit user query
        submit_query = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
        )
        submit_query.click()
        time.sleep(10)

        

    except Exception as e:
        print(f'An error occurred: {str(e)}')
    # driver.find_element(By.ID, "input28").send_keys("hello@gmail.com")
    # query all test methods and select test cases based on specific name: pytest -k MethodName -v -s
    # -k: method names execution, -s logs in terminal output, -v verbosity in terminal metadata output
    # Run specific file name: pytest test_web_app_automation.py -v 
    # button = driver.find_element(By.XPATH, "//input[@type=submit]")
    # print("\n\n Submit button was found \n\n")
    
    # button = driver.find_element(By.NAME, "password").send_keys("12345")
    # driver.find_element(By.NAME, "checkbox").click()

    # XPATH format: //tagname[@attribute='value'] //input[@type='submit']
    # searching for an element using their respective XPATH
    # driver.find_element(By.XPATH, "//input[@type='submit']").click()

    # CSSSelector format: tagname[attribute='value'] | #id, .classname
    # third element in xpath: (//input[@type='text'])[n-element]
    # self.driver.find_element(By.CSSSELECTOR, "input[name='name]").send_keys("Matheus")

    # store successful account creation text into a message var
    # message = driver.find_element(By.CLASS_NAME, "alert-success").text
    # print(message)
    # assert "Success" in message
