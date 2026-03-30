from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver  = webdriver.Chrome()
url = "https://the-internet.herokuapp.com/windows"
driver.get(url)
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.LINK_TEXT,"Click Here").click()

openWindows = driver.window_handles

driver.switch_to.window(openWindows[1])
newWindow=driver.find_element(By.TAG_NAME,"h3")
print(newWindow.text)
driver.close()
driver.switch_to.window(openWindows[0])
assert "Opening a new window" == driver.find_element(By.TAG_NAME,"h3").text
