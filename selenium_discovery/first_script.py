import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from  selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# chrome driver interprets webdriver and interacts with Chrome browser
# Selenium has a webdriver for all Chrome drivers. It calls the respective Chrome driver from chrome library needed for the command to invoke Chrome
driver = webdriver.Chrome()

driver.get("https://learning.oreilly.com/home/")

time.sleep(4)


# try:
#     driver.get("https://www.selenium.dev/selenium/web/web-form.html")
#     # Wait for the text box to be present in the DOM
#     text_box = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.NAME, "my-text"))
#     )
#     # text_box = driver.find_element(by=By.ID, value="id")
    
#     title = driver.title

#     driver.implicitly_wait(2)

#     submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")

#     text_box.send_keys("Selenium")
#     submit_button.click()

#     message = driver.find_element(by=By.ID, value="message")
#     text = message.text
#     driver.implicitly_wait(5)
# finally:
#     driver.quit()