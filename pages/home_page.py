# pages/home_page.py
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    # Locators
    SEARCH_BOX = (By.ID, 'search-box')
    WOMAN_BUTTON = (By.ID, 'search-button')
    MEN_BUTTON = (By.CLASS_NAME, 'men-button')
    SHOP_BUTTON = (By.CLASS_NAME, 'gift-products')

    # Add more locators as needed

    # Methods
    def __init__(self, driver: object) -> object:
        super().__init__(driver)
        self.SEARCH_BUTTON = None
        self.SHOP_BUTTON = None
        self.MEN_APPAREL = None
        self.WOMAN_APPAREL = None

    def search_for_product(self, keyword):
        self.enter_text(self.SEARCH_BOX, keyword)
        self.click_element(self.SEARCH_BUTTON)