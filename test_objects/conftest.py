# tests/conftest.py
import pytest
from driver_factory import DriverFactory, create_driver
from pages.home_page import HomePage
from pages.account_page import AccountPage
from pages.checkout_page import CheckoutPage
from pages.cart_page import CartPage
from pages.product_page import ProductPage

# Fixture for the WebDriver
def create_driver():
    pass


@pytest.fixture
def driver():
    driver = create_driver()
    yield driver
    driver.quit()

# Fixtures for different PageObjects
@pytest.fixture
def home_page(driver):
    return HomePage(driver)

@pytest.fixture
def account_page(driver):
    return AccountPage(driver)

@pytest.fixture
def checkout_page(driver):
    return CheckoutPage(driver)

@pytest.fixture
def cart_page(driver):
    return CartPage(driver)

@pytest.fixture
def product_page(driver):
    return ProductPage(driver)
