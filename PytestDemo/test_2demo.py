import pytest

def test_first_method(): # test method also start with test_
    print("First programming")

@pytest.mark.smoketest
def test_second_method():
    msg = "Hello"
    try:
        assert type(msg) == str
    except AssertionError:
        print(AssertionError)
#@pytest.mark.skip
def test_third_method():
    a=2
    b=3
    assert a+b == 10, "does not match"

@pytest.mark.xfail
def test_fourth_method():
    a=2
    b=3
    assert a+b == 5, "does not match"