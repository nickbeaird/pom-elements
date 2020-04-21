import pytest
from selenium import webdriver


@pytest.fixture(scope="module")
def selenium_chrome(request):
    """Create a session of Selenium Chrome that can used across an entire file of tests."""
    _driver = webdriver.Chrome()
    _driver.maximize_window()
    _driver.get("https://www.google.com")
    request.addfinalizer(_driver.quit)
    return _driver
