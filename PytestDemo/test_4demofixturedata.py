import pytest

@pytest.mark.usefixtures("load_data")
class TestLoadData:
    list_item = []
    def test_fixture1(self,load_data): # argument of load data is required when fixture is returning some data
                                       # therefore it is mandatory to add fixture name
        for item in load_data: # different ways to print data
            print(item)
        print(load_data[0])
        print(load_data[1])
        print(load_data[2])
        print("*****************")
@pytest.mark.usefixtures("crossBrowser")
def test_cross_browser(crossBrowser):
        print(crossBrowser)

@pytest.mark.usefixtures("CrossBrowsers")
def test_cross_browsers(CrossBrowsers):
        print(CrossBrowsers[0])
        print(CrossBrowsers[1])