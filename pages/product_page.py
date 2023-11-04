# pages/product_page.py
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ProductPage(BasePage):
    # Locators
    PRODUCT_TITLE = (By.CLASS_NAME, 'product-title')
    ADD_TO_CART_BUTTON = (By.ID, 'add-to-cart-button')
    PRODUCT_DESCRIPTION = (By.CLASS_NAME, 'product-description')
    RELATED_PRODUCTS = (By.CLASS_NAME, 'related-products')
    # Add more locators as needed

    # Methods
    def get_product_title(self):
        return self.find_element(self.PRODUCT_TITLE).text

    def add_product_to_cart(self):
        self.click_element(self.ADD_TO_CART_BUTTON)

    def get_product_description(self):
        return self.find_element(self.PRODUCT_DESCRIPTION).text

    def view_related_products(self):
        self.scroll_to_element(self.RELATED_PRODUCTS)
    # Add more methods as needed
