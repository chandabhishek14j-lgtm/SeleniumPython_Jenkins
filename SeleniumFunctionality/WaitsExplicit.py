from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
url = "https://rahulshettyacademy.com/seleniumPractise"
driver.get(url)
wait = WebDriverWait(driver, 10)

driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("be")
time.sleep(3) # here I am using sleep as return type of find_elemts is a list and as soon as
# list is retrieved it will proceed even if the list is empty
resultsList = driver.find_elements(By.XPATH,"//div[@class='products']/div")
productList = driver.find_elements(By.XPATH,"//div[@class='products']/div/h4")
iTemList = []
for itm in productList:
    iTemList.append(itm.text)
print(iTemList)
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
receivedCode = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
print(receivedCode.text)

prices = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p")
totalAmount = 0
for item in prices:
    totalAmount = totalAmount + int(item.text)
print(totalAmount)

ReceivedAmount = int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)
assert ReceivedAmount == totalAmount
time.sleep(3)
discount = float(driver.find_element(By.CSS_SELECTOR, ".discountAmt").text)
assert discount < ReceivedAmount