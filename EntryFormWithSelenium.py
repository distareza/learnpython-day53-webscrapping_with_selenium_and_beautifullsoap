from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
import time

CHROME_DRIVER_PATH = "C:/apps/chromedriver_win32/chromedriver.exe"
GOOGLE_FORM_LINK = "https://forms.gle/AeeskQ9cdV83phhWA"

xpath_location_input = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'
xpath_price_input = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'
xpath_link_input = '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'
xpath_button = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span'


class EntryForm:

    def __init__(self):
        caps = DesiredCapabilities().CHROME
        caps["pageLoadStrategy"] = "normal"  #  Waits for full page load
        #caps["pageLoadStrategy"] = "none"  # Do not wait for full page load

        self.selenium_service = Service(executable_path=CHROME_DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.selenium_service, desired_capabilities=caps)

    def entry(self, input_link, input_price, input_address):
        self.driver.get(GOOGLE_FORM_LINK)

        time.sleep(2)
        address = self.driver.find_element(By.XPATH, xpath_location_input)
        price = self.driver.find_element(By.XPATH, xpath_price_input)
        link = self.driver.find_element(By.XPATH, xpath_link_input)
        submit_button = self.driver.find_element(By.XPATH, xpath_button)

        address.send_keys(input_address)
        price.send_keys(input_price)
        link.send_keys(input_link)
        submit_button.click()
