import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from login_page import LoginPage
from product_page import ProductsPage
from cart_page import CartPage
from checkout_page import CheckoutPage

@pytest.fixture
def driver():
    '''Invoke driver'''
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

def test_valid_login(driver):
    '''Tests the valid login using the standard user'''
    username = "standard_user"
    password = "secret_sauce"
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login(username, password)

    # wait until the products page is loaded
    WebDriverWait(driver, 10).until(EC.url_contains("inventory.html"))
    assert "inventory.html" in driver.current_url

def test_complete_checkout(driver):
    '''Performs complete end-to-end checkout process'''
    username = "standard_user"
    password = "secret_sauce"
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login(username, password)
    WebDriverWait(driver, 10).until(EC.url_contains("inventory.html"))

    product_page = ProductsPage(driver)
    product_page.add_SLBackpack_to_cart()
    product_page.go_to_cart()

    cart_page = CartPage(driver)
    cart_page.click_checkout()

    checkout_page = CheckoutPage(driver)
    first_name = "Saurav"
    last_name = "Shah"
    postal_code = "54500"
    checkout_page.fill_checkout_form(first_name, last_name, postal_code)
    checkout_page.complete_order()
    confirmation_text = checkout_page.get_confirmation_text()
    assert "Thank you for your order!" in confirmation_text