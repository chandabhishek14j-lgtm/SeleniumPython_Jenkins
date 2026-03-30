from selenium.webdriver.support import expected_conditions as EC
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

class CheckouItem:
    def __init__(self, driver):
        self.driver = driver

        self.visible_item_locator = (By.XPATH, "//app-card/div[@class='card h-100']")
        self.title_locator = (By.XPATH, ".//h4[@class='card-title']/a")
        self.add_btn_locator = (By.XPATH, ".//button[@class='btn btn-info']")
        self.dynamix_text_locator = (By.XPATH, "//a[text()='India']")
        self.purchase_locator = (By.CSS_SELECTOR, ".btn.btn-success.btn-lg")

    def checkout(self):
        wait = WebDriverWait(self.driver, 10)
        final_checkout = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".btn.btn-success")))
        final_checkout.click()