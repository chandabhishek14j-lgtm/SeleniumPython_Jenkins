from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time
driver = webdriver.Chrome()
url = "https://rahulshettyacademy.com/client"
driver.maximize_window()
driver.get(url)
driver.find_element(By.LINK_TEXT, "Forgot password?").click()
driver.find_element(By.XPATH, "//form/div[1]/input[@type='email']").send_keys("abhishekchand14j@gmail.com")
driver.find_element(By.XPATH, "//form/div[2]/input[@type='password']").send_keys("Alpha@4321")
driver.find_element(By.XPATH, "//form/div[3]/input[@type='password']").send_keys("Alpha@4321")
driver.find_element(By.XPATH, "//form/div[4]/button[@type='submit']").click()

time.sleep(10)