# pages/checkout_page.py
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckoutPage(BasePage):
    # Locators
    SHIPPING_ADDRESS = (By.ID, 'shipping-address')
    BILLING_ADDRESS = (By.ID, 'billing-address')
    PAYMENT_METHOD = (By.ID, 'payment-method')
    ORDER_SUMMARY = (By.ID, 'order-summary')
    SHIPPING_METHODS = (By.ID, 'shipping-methods')
    PROMO_CODE_FIELD = (By.ID, 'promo-code-field')
    APPLY_PROMO_BUTTON = (By.ID, 'apply-promo-button')
    PLACE_ORDER_BUTTON = (By.ID, 'place-order-button')
    ORDER_CONFIRMATION_MESSAGE = (By.CLASS_NAME, 'order-confirmation-message')
    ERROR_MESSAGE = (By.CLASS_NAME, 'error-message')
    # Add more locators as needed

    # Methods
    def enter_shipping_address(self, address):
        self.enter_text(self.SHIPPING_ADDRESS, address)

    def enter_billing_address(self, address):
        self.enter_text(self.BILLING_ADDRESS, address)

    def select_payment_method(self, method):
        payment_methods = self.find_elements(self.PAYMENT_METHOD)
        for option in payment_methods:
            if option.text == method:
                option.click()
                break

    def view_order_summary(self):
        self.scroll_to_element(self.ORDER_SUMMARY)

    def select_shipping_method(self, method):
        shipping_methods = self.find_elements(self.SHIPPING_METHODS)
        for option in shipping_methods:
            if option.text == method:
                option.click()
                break

    def apply_promo_code(self, code):
        self.enter_text(self.PROMO_CODE_FIELD, code)
        self.click_element(self.APPLY_PROMO_BUTTON)

    def place_order(self):
        self.click_element(self.PLACE_ORDER_BUTTON)

    def get_order_confirmation_message(self):
        return self.find_element(self.ORDER_CONFIRMATION_MESSAGE).text

    def get_error_message(self):
        return self.find_element(self.ERROR_MESSAGE).text
    # Add more methods as needed
    def find_elements(self, PAYMENT_METHOD):
        pass
