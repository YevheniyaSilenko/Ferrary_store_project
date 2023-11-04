# driver_factory.py
from selenium import webdriver
from config.config import Config

class DriverFactory:
    pass


def create_driver():
    driver = webdriver.Chrome(executable_path=Config.DRIVER_PATH)
    driver.maximize_window()
    return driver
