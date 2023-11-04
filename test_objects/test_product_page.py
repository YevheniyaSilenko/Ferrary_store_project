import pytest
from selenium import webdriver
from pages.product_page import ProductPage

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def product_page(driver):
    page = ProductPage(driver)
    driver.get('https://store.ferrari.com/en-us/women/apparel/sweaters-and-sweatshirts')  # Replace with the URL of your product page
    yield page

def test_get_product_title(product_page):
    product_title = product_page.get_product_title()
    assert product_title == "https://store.ferrari.com/en-us/polo-necks_cod1647597321680955.html#dept=Jumper-Sweatshirts_APPAREL_W"  # Replace with the expected product title

def test_add_product_to_cart(product_page):
    product_page.add_product_to_cart()
    # Add assertions to check if the product was successfully added to the cart

def test_get_product_description(product_page):
    product_description = product_page.get_product_description()
    assert "Product description" in product_description  # Replace with expected description content

def test_view_related_products(product_page):
    product_page.view_related_products()
    # Add assertions to check if the related products section is visible and active

# Add more test cases as needed
