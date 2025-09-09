from locust import HttpUser, task, between, events
import os
import webbrowser
from bs4 import BeautifulSoup

class UserBehavior(HttpUser):
    wait_time = between(1,5)

    def on_start(self):
        print("Step One: Initiate Load Test...")
    
    @task
    def load_test_endpoint(self):

        home_page_test = True
        if home_page_test == True:
            # Submit API request Home page
            home_response = self.client.get("/")

            if home_response.status_code == 200:
                
                # Positive Test #1: Output current URL
                payload_url = home_response.url
                print(f"\nPositive Test #1:\nCurrent URL being hit: {payload_url}\n")

                # Parse response content
                soup = BeautifulSoup(home_response.content, 'html.parser')
                title_tag = soup.title
                
                # Positive Test #2: Output dev-aizone element
                if title_tag:
                    print(f"\nPositive Test #2:\nPage title is: {title_tag}")
                else:
                    print("Specified element was not found")
            else: 
                print(f"Failed to land on page, status code: {home_response.status_code}")

        chat_interface_test = False
        if chat_interface_test == True:
            # API request to Chat Interface
            chat_interface_response = self.client.get("/app/text")

            if chat_interface_response.status_code == 200:
                
                # Positive Test #1: Output current URL
                payload_url = chat_interface_response.url
                print(f"\n\nPositive Test #3:\nCurrent URL being hit: {payload_url}\n")

                # Parse response content
                soup = BeautifulSoup(chat_interface_response.content, 'html.parser')

                print(soup.prettify())

                # Extract the <h2> tag with the specific class
                h2_tag = soup.find('h2', class_='text-3xl text-primary font-slab')
                
                if h2_tag:
                    # Extract and print the text from the <h2> tag
                    extracted_text = h2_tag.get_text(strip=True)
                    print(f"Extracted text: {extracted_text}")
                else:
                    print("The specified <h2> tag was not found.")

                # Additional: Print all <h2> tags for debugging
                all_h2_tags = soup.find_all('h2')
                for tag in all_h2_tags:
                    print(tag.get_text(strip=True))  


                title_of_interest = False
                if title_of_interest == True:

                    title_tag = soup.title
                    
                    # Positive Test #2: Output dev-aizone element
                    if title_tag:
                        print(f"\nPositive Test #4:\nPage title is: {title_tag}\n\n")
                    else:
                        print("Specified element was not found")
            else: 
                print(f"Failed to land on page, status code: {chat_interface_response.status_code}")

    
    def on_stop(self):
        print('Step Three: End Load Test...')

@events.quitting.add_listener
def open_report(environment, **kwargs):
    report_path = os.path.abspath("ailz-locustreport.html")

    if os.path.exists(report_path):
        print(f"Opening report: {report_path}")
        webbrowser.open(f"file://{report_path}")
    else:
        print(f"Report not found at: {report_path}")


# class WebsiteUser(HttpUser):
#     tasks = {UserBehavior: 1}
#     wait_time = between(1, 5)

# class QuickstartUser(HttpUser):
#     wait_time = between(1,5)

#     def on_start(self):
#         print("Step One: Initiate Load Test...")

#     # Perform load test for API #1
#     @task
#     def hello_world(self):
#         self.client.get("/hello-world")
    
#     # Perform load for API #2
#     @task
#     def getTimeDetails(self):
#         self.client.get("/getMyTime")

    
#     def on_stop(self):
#         print('Step Two: End Load Test...')