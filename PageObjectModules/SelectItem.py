from selenium.webdriver.support import expected_conditions as EC
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from utils.BrowserUtils import BrowserUtils

class SelectItem(BrowserUtils):
    def __init__(self, driver):
        super().__init__(driver)# Here super is referring to parent class constructor
        self.driver = driver
        self.visible_item_locator = (By.XPATH, "//app-card/div[@class='card h-100']")
        self.title_locator = (By.XPATH, ".//h4[@class='card-title']/a")
        self.add_btn_locator = (By.XPATH, ".//button[@class='btn btn-info']")
        self.dynamix_text_locator = (By.XPATH, "//a[text()='India']")
        self.purchase_locator = (By.CSS_SELECTOR, ".btn.btn-success.btn-lg")

    def select_item(self, product_name):
        # using partial characters in CSS or XPATH to obtain element
        """
        xpath: //a[contains(@href,'shop')] | //tag_name[contains(@attribute_name, 'attribute_value')]
        css  : a[href*='shop'] | tag_name[attribute_name*='attribute_value']
        """
        wait = WebDriverWait(self.driver, 10)
        shop_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[href*='shop']")))
        shop_button.click()
        shop_url = self.driver.current_url
        assert "shop" in shop_url

        visible_items = self.driver.find_elements(*self.visible_item_locator)
        for item in visible_items:
            title = self.driver.find_element(*self.title_locator).text
            if title != product_name:
                print(product_name,"!! Pass")
            else:
                add_button = self.driver.find_element(*self.add_btn_locator)
                add_button.click()

        checkout = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".nav-link.btn.btn-primary")))
        checkout.click()

