import pytest
from selenium import webdriver


@pytest.fixture # This is Test level will run before each test when defined
def setup():
    print("setup Before done")
    yield
    print("After execution done")

@pytest.fixture(scope="class") # This is class level run once when class is engaged and
                               # yield after execution of class is done
def setup_class():
    print("setup Before Class done")
    yield
    print("After execution Class done")

@pytest.fixture
def load_data():

    print("Load data Before Test")
    return ["rahul", "shetty", "rahulshetty.com"]

@pytest.fixture(params=["chrome", "firefox"]) # parameterization of fixture i.e. passing params in fixtures
def crossBrowser(request):
    return request.param

# Parameterizing but with multiple values
@pytest.fixture(params=[("chrome", "Abhishek"), ("firefox", "Chand")])
def CrossBrowsers(request):
    return request.param