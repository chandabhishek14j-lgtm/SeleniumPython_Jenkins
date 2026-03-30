# fixture setup is mentioned in conftest file available for all test_ files to use
import pytest

def test_fixture(setup):
    print("test fixture")

# if we have multiple test cases then instead of defining ficture for all we can wrap...
#... all the test cases inside a class and define it only once

@pytest.mark.usefixtures("setup_class")
class Test_Fixture_Class:
    def test_fixture1(self):
        print("test 1 fixture")

    def test_fixture2(self):
        print("test 2 fixture")

    def test_fixture3(self):
        print("test 3 fixture")

    def test_fixture4(self):
        print("test 4 fixture")