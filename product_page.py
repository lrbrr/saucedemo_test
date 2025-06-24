from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductsPage:
    def __init__(self, driver):
        self.driver = driver
        self.sl_backpack_add_to_cart_button = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.cart_icon = (By.ID, "shopping_cart_container")
        self.sl_backpack_remove_from_cart_button = (By.ID, "remove-sauce-labs-backpack")

    def add_SLBackpack_to_cart(self):
        '''Add Sauce Labs Backpack to the cart'''
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.sl_backpack_add_to_cart_button)).click()

    def remove_SLBackpack_from_cart(self):
        '''Remove Sauce Labs Backpack to the cart'''
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.sl_backpack_remove_from_cart_button)).click()
    
    def go_to_cart(self):
        '''Navigate to the cart page'''
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.cart_icon)).click()