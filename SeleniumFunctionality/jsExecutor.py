#for example selenium does not provide any method for scroll but using js we can
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
#if you want to run in headless mode
chromeOption = webdriver.ChromeOptions()
chromeOption.add_argument("--headless")
chromeOption.add_argument("--ignore-certificate-errors") #this flag is used for passing pops...
#... happens to be there on website like security alerts or disclaimer 
driver = webdriver.Chrome(options=chromeOption)
wait = WebDriverWait(driver, 10)
driver.implicitly_wait(10)
driver.maximize_window()
url = "https://rahulshettyacademy.com/AutomationPractice/"
driver.get(url)

driver.execute_script("window.scroll(0,document.body.scrollHeight)")
#by this selenium will tell the browser to run this js script
driver.get_screenshot_as_file("screenshot.png")
time.sleep(2)