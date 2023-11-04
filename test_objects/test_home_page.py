import pytest
from selenium import webdriver
from pages.home_page import HomePage


# Set up a fixture to initialize the web driver and open the home page
@pytest.fixture
def browser():
    driver = webdriver.Chrome()  # You can use any other web driver you prefer
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_search_for_product(browser):
    home_page = HomePage(browser)
    home_page.open("https://store.ferrari.com/en-us/")  # Replace with your actual website URL

    keyword = "leather-jackets"
    home_page.search_for_product(keyword)

    # Add assertions to verify that the search results are displayed correctly
    # For example, check if search results include the keyword in their descriptions.


def test_click_on_woman_apparel(browser):
    home_page = HomePage(browser)
    home_page.open("https://store.ferrari.com/en-us/women/apparel")

    home_page.click_on_woman_apparel()



def test_click_on_men_apparel(browser):
    home_page = HomePage(browser)
    home_page.open("https://store.ferrari.com/en-us/men/apparel")

    home_page.click_on_men_apparel()

    # Add assertions to verify that clicking on the "Men Apparel" button scrolls to the men's apparel section.


def test_click_on_gift_inspiration(browser):
    home_page = HomePage(browser)
    home_page.open("https://store.ferrari.com/en-us/gift-inspiration/gift-ideas-for-collectors")

    home_page.click_on_gift_inspiration()

    # Add assertions to verify that clicking on the "Shop for Gift Products" button scrolls to the gift products section.

# Add more test cases as needed
