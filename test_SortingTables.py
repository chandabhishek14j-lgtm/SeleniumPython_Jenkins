from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
def test_sort_table(browser_instance):
    driver = browser_instance

    wait = WebDriverWait(driver, 10)
    browserSortedList = []
    url = "https://rahulshettyacademy.com/seleniumPractise/#/offers"
    driver.get(url)
    driver.implicitly_wait(10)
    # click on the column header

    # assert newList == veggieList this should be true
    columnHeader = driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']")
    columnHeader.click()
    # collect all names in one list >-- veggieList (Already Sorted)
    veggieList = driver.find_elements(By.XPATH, "//tr/td[1]")
    for item in veggieList:
        browserSortedList.append(item.text)
    newList = browserSortedList.copy()
    # sort the list >-- newList via python
    browserSortedList.sort()

    assert browserSortedList == newList

    print(browserSortedList)


