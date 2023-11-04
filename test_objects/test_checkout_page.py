import pytest
from selenium import webdriver
from pages.checkout_page import CheckoutPage

@pytest.fixture(scope="class")
def driver():
    driver = webdriver.Chrome()
    driver.get('https://store.ferrari.com/us/OnePageCheckout/Cart')  # Replace with your website URL
    yield driver
    driver.quit()

@pytest.fixture(scope="class")
def checkout_page(driver):
    return CheckoutPage(driver)

class TestCheckoutPage:
    def test_enter_shipping_address(self, checkout_page):
        address = "123 Shipping St, Shipping City"
        checkout_page.enter_shipping_address(address)
        # Add assertions to check if the address was entered correctly

    def test_enter_billing_address(self, checkout_page):
        address = "456 Billing St, Billing City"
        checkout_page.enter_billing_address(address)
        # Add assertions to check if the address was entered correctly

    def test_select_payment_method(self, checkout_page):
        method = "Credit Card"
        checkout_page.select_payment_method(method)
        # Add assertions to check if the payment method was selected correctly

    def test_view_order_summary(self, checkout_page):
        checkout_page.view_order_summary()
        # Add assertions to check if the order summary is visible

    def test_select_shipping_method(self, checkout_page):
        method = "Express Shipping"
        checkout_page.select_shipping_method(method)
        # Add assertions to check if the shipping method was selected correctly

    def test_apply_promo_code(self, checkout_page):
        promo_code = "DISCOUNT123"
        checkout_page.apply_promo_code(promo_code)
        # Add assertions to check if the promo code was applied successfully

    def test_place_order(self, checkout_page):
        checkout_page.place_order()
        # Add assertions to check if the order was placed successfully

    def test_get_order_confirmation_message(self, checkout_page):
        confirmation_message = checkout_page.get_order_confirmation_message()
        # Add assertions to check the content of the order confirmation message

    def test_get_error_message(self, checkout_page):
        error_message = checkout_page.get_error_message()
        # Add assertions to check the content of the error message
