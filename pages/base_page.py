# pages/base_page.py
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from config.config import Config

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = Config.BASE_URL

    def open(self, url):
        self.driver.get(url)

    def find_element(self, by, value):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((by, value)))

    def click_element(self, by, value):
        element = self.find_element(by, value)
        element.click()

    def enter_text(self, by, value, text):
        element = self.find_element(by, value)
        element.send_keys(text)
