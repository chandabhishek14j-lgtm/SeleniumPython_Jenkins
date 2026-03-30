#goal is to go on a website select some items and purchase them
from selenium.webdriver.support.ui import WebDriverWait
from PageObjectModules.LoginPage import LoginPage
from PageObjectModules.SelectItem import SelectItem
from PageObjectModules.CheckoutItem import CheckouItem
from PageObjectModules.PurchaseItem import PurchaseItem
import json
import pytest

json_file_data = "C:\\Users\\AVITA\\Desktop\\SeleniumPython\\DataCollection\\test_E2Echeckout.json"
with open(json_file_data) as file:
    data = json.load(file) # This will convert the JSON file in dictionary so that python can access it
    test_data = data["data"] # this is now a list fetched from the dictionary

@pytest.mark.smoke
@pytest.mark.parametrize("list_item",test_data) #this expects list only and this will be stored in variable mentioned in string
def test_e2e_framework(browser_instance, list_item):#the parametrized variable is passed as argument then only it can be used
    driver = browser_instance
    driver.implicitly_wait(10)
    wait = WebDriverWait(driver, 10)

    Login = LoginPage(driver)
    Login.login(list_item["userEmail"], list_item["userPassword"])
    print(Login.get_title())

    select_item = SelectItem(driver)
    select_item.select_item(list_item["productName"])
    print(Login.get_title())

    final_checkout = CheckouItem(driver)
    final_checkout.checkout()

    purchase = PurchaseItem(driver)
    purchase.purchase()
