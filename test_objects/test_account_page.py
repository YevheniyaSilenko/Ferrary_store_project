import pytest
from selenium import webdriver
from pages.account_page import AccountPage


# Set up a fixture to initialize the web driver and open the account page
@pytest.fixture
def browser():
    driver = webdriver.Chrome()  # You can use any other web driver you prefer
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


# login:prencezza12@gmail.com, password:Canima_222
def test_get_account_information(browser):
    account_page = AccountPage(browser)
    account_page.open("https://store.ferrari.com/en-us/Account/Overview")  # Replace with your actual account page URL

    account_info = account_page.get_account_information()

    # Add assertions to verify that the account information is displayed correctly.
    # For example, check if the account information contains the user's name, email, and other relevant details.


def test_view_order_history(browser):
    account_page = AccountPage(browser)
    account_page.open("https://store.ferrari.com/en-us/Account/Orders")

    account_page.view_order_history()

    # Add assertions to verify that clicking on the "Order History" button navigates to the expected page or takes
    # the expected action.


def test_change_password(browser):
    account_page = AccountPage(browser)
    account_page.open("https://example.com/account")

    account_page.change_password()

    # Add assertions to verify that clicking on the "Change Password" button navigates to the password change page or takes the expected action.


def test_manage_address_book(browser):
    account_page = AccountPage(browser)
    account_page.open("https://store.ferrari.com/en-us/Account/AddressBook")

    account_page.manage_address_book()

    # Add assertions to verify that the address book section is visible or that it scrolls into view.


def test_logout(browser):
    account_page = AccountPage(browser)
    account_page.open("https://login.ferrari.com/account/logout")

    account_page.logout()

    # Add assertions to verify that clicking on the "Logout" button logs the user out and navigates to the login page.

# Add more test cases as needed
