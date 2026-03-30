from selenium.webdriver.support import expected_conditions as EC
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

class PurchaseItem:
    def __init__(self, driver):
        self.driver = driver

        self.visible_item_locator = (By.XPATH, "//app-card/div[@class='card h-100']")
        self.title_locator = (By.XPATH, ".//h4[@class='card-title']/a")
        self.add_btn_locator = (By.XPATH, ".//button[@class='btn btn-info']")
        self.dynamix_text_locator = (By.XPATH, "//a[text()='India']")
        self.purchase_locator = (By.CSS_SELECTOR, ".btn.btn-success.btn-lg")

    def purchase(self):

        wait = WebDriverWait(self.driver, 10)
        location = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".validate")))
        location.send_keys("India")
        suggestion = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[text()='India']")))
        dynamicText = self.driver.find_element(*self.dynamix_text_locator).get_attribute("textContent")
        try:
            assert dynamicText == "India"
            print("Success!!!!")
        except AssertionError:
            print("Test Fail!!!!")
        suggestion.click()

        purchase = self.driver.find_element(*self.purchase_locator)
        purchase.click()

        try:
            alert = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert")))
            print("Success message:", alert.text)
        except TimeoutException:
            print("No error alert found")
            print("Purchase not Done")