from selenium import webdriver
import time

driver = webdriver.Chrome() #invoke Chrome browser

driver.get("https://google.com")
driver.maximize_window()
print(driver.title)
print(driver.current_url)

time.sleep(4)