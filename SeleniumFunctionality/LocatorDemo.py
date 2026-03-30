
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")
#locators to find elements : ID, NAME, Xpath, CSSSelector, className, text
#driver.find_element(By.NAME, "name").send_keys("AbhishekChand")
driver.find_element(By.CSS_SELECTOR,"input[name='name']").send_keys("Abhishek")
driver.find_element(By.NAME, "email").send_keys("abhishek@google.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("12345678")
driver.find_element(By.ID, "exampleCheck1").click()
#CSSSelector syntax: tag_name[attribute='value'] : #id_value : #class_value these are three ways to find element
#xpath syntax: //tag_name[@attribute_name='value']
#if using xpath and multiple elements matching eg:"//input[@type='text']" 4 elements matching...
#then (//input[@type='text'])[no.of that element] this will work too
driver.find_element(By.XPATH, "//input[@type='text']").send_keys("Chand")
driver.find_element(By.XPATH, "//input[@type='submit']").send_keys(Keys.RETURN)
driver.find_element(By.XPATH, "//input[@type='text']").clear()
message = driver.find_element(By.CLASS_NAME, "alert-success").text
str1="Success"
if str1 in message:
    print("Test Pass:",message)
else:
    print("Test Fail:",message)
# verify via assertion
"""
assert str1 in message
"""

print(driver.current_url)

time.sleep(10)
