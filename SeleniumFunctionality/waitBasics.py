from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.implicitly_wait(5) # will globally wait for 5 seconds and will continue immediately after object is find
url = "https://rahulshettyacademy.com/seleniumPractise"
driver.get(url)
driver.maximize_window()

driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("be")
time.sleep(3) # here I am using sleep as return type of find_elemts is a list and as soon as
# list is retrieved it will proceed even if the list is empty
resultsList = driver.find_elements(By.XPATH,"//div[@class='products']/div")
count = len(resultsList)
assert count >0
buttons = driver.find_elements(By.XPATH,"//div[@class='products']/div/div/button")
for button in buttons:
    button.click()

promoCode = "rahulshettyacademy"
driver.find_element(By.XPATH,"//a[@class='cart-icon']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()

cUrl = driver.current_url

driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys(promoCode)
driver.find_element(By.CSS_SELECTOR, ".promoBtn").send_keys(Keys.RETURN)
print(driver.find_element(By.CLASS_NAME, "promoInfo").text)




time.sleep(5)