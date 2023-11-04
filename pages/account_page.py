# pages/account_page.py
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class AccountPage(BasePage):
    # Locators
    ACCOUNT_INFO = (By.ID, 'account-info')
    ORDER_HISTORY = (By.CLASS_NAME, 'order-history')
    CHANGE_PASSWORD_BUTTON = (By.ID, 'change-password-button')
    ADDRESS_BOOK = (By.CLASS_NAME, 'address-book')
    LOGOUT_BUTTON = (By.ID, 'logout-button')
    # Add more locators as needed
  # Methods
    def get_account_information(self):
        return self.find_element(self.ACCOUNT_INFO).text

    def view_order_history(self):
        self.click_element(self.ORDER_HISTORY)

    def change_password(self):
        self.click_element(self.CHANGE_PASSWORD_BUTTON)

    def manage_address_book(self):
        self.scroll_to_element(self.ADDRESS_BOOK)

    def logout(self):
        self.click_element(self.LOGOUT_BUTTON)
    # Add more methods as needed