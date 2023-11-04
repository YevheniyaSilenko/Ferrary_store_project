# pages/cart_page.py
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):
    # Locators
    CART_ITEMS = (By.CLASS_NAME, 'cart-item')
    CHECKOUT_BUTTON = (By.ID, 'checkout-button')
    EMPTY_CART_MESSAGE = (By.CLASS_NAME, 'empty-cart-message')
    # Add more locators as needed

    # Methods
    def get_cart_items_count(self):
        return len(self.find_elements(self.CART_ITEMS))

    def proceed_to_checkout(self):
        self.click_element(self.CHECKOUT_BUTTON)

    def get_empty_cart_message(self):
        return self.find_element(self.EMPTY_CART_MESSAGE).text
    # Add more methods as needed