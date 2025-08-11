import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# needs to include testing for Chrome, Mozilla, Edge, and Safari
class ChromeTestCase(unittest.TestCase):
    # use webdriver to execute Chrome file
    def setUp(self):
        self.driver = webdriver.Chrome()

    # use webdriver to send get request to specific URL
    def test_page_title(self):
        # self.driver.get("https://developer.mozilla.org/en-US/")
        self.driver.get('https://selenium.dev/documentation')
        # WebDriverWait(self.driver, 2).until(EC.title_contains("MDN Web Docs"))
        self.assertIn('Selenium', self.driver.title)
    
    def test_page_click_article(self):
        # self.driver.get("https://developer.mozilla.org/en-US/")
        self.driver.get('https://selenium.dev/documentation')

        # get current URL when directed elsewhere by pop-up
        print(self.driver.current_url)

        # wait until elements are present
        elem = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, 'm-documentationwebdriver'))
            # EC.presence_of_element_located((By.CSS_SELECTOR, 'button.primary.mdn-plus-subscribe-link'))
        )
        elem.click()
        self.assertIn('WebDriver', self.driver.title)
        

        # tile_elements = self.driver.find_element(By.CLASS_NAME, 'tile-container')
        # elem = self.driver.find_element(By.CLASS_NAME, 'article-tile')
        # elem.click()
        time.sleep(2)
    
    def test_account_login(self):
        self.driver.find_element(By.NAME, "email").send_keys("hello@gmail.com")
        self.driver.find_element(By.NAME, "password").send_keys("12345")
        self.driver.find_element(By.NAME, "checkbox").click()

        # XPATH format: //tagname[@attribute='value'] //input[@type='submit']
        # searching for an element using their respective XPATH
        self.driver.find_element(By.XPATH, "//input[@type='submit']").click()

        # CSSSelector format: tagname[attribute='value'] | #id, .classname
        # third element in xpath: (//input[@type='text'])[n-element]
        # self.driver.find_element(By.CSSSELECTOR, "input[name='name]").send_keys("Matheus")

        # store successful account creation text into a message var
        message = self.driver.find_element(By.CLASS_NAME, "alert-success").text
        print(message)
        assert "Success" in message

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
