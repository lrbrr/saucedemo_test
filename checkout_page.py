from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name_input = (By.ID, "first-name") 
        self.last_name_input = (By.ID, "last-name")
        self.postal_code_input = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.finish_button = (By.ID, "finish")
        self.confirmation_text = (By.CLASS_NAME, "complete-header")
    
    def fill_checkout_form(self, first_name, last_name, postal_code):
        '''Fills the checkout form'''
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.first_name_input)).send_keys(first_name)
        self.driver.find_element(*self.last_name_input).send_keys(last_name)
        self.driver.find_element(*self.postal_code_input).send_keys(postal_code)
        self.driver.find_element(*self.continue_button).click()
    
    def complete_order(self):
        '''Completes the order'''
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.finish_button)).click()
    
    def get_confirmation_text(self):
        '''Returns the text of the order confirmation'''
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.confirmation_text)).text