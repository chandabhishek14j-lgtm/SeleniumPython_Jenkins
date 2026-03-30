from selenium.webdriver.common.by import By
from utils.BrowserUtils import BrowserUtils
import pytest

# I want to call this page for login functionality in test_E2Echeckout.py
#therefore have to call it with a driver otherwise driver will be unrecognizable by the login class
class LoginPage(BrowserUtils):
    def __init__(self, driver):
        super().__init__(driver)  # Here super is referring to parent class constructor
        self.driver = driver
        self.username_input = (By.ID, "username")
        self.password_input = (By.ID, "password")
        self.signin_input = (By.ID, "signInBtn")
        pass

    def login(self, username, password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        sign_in = self.driver.find_element(*self.signin_input)
        sign_in.click()
        # use of * in find elements is that it breaks down the elements in tuple into arguments...
        #... as find elements understand arguments and not tuple

