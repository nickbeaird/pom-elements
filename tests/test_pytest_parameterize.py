import time

import pytest
from selenium import webdriver
from selenium_xpath.base_tag import BaseTag


@pytest.mark.parametrize(
    "browser", [webdriver.Chrome(), webdriver.Firefox(), webdriver.Safari()]
)
def test_browser_instantiation(browser):
    """Verify that we can parameterize browser testing."""
    browser.get("http://www.yahoo.com")
    search = BaseTag(xpath="//input", html_id="header-search-input", webdriver=browser)
    assert search.is_visible(timeout=2)
    browser.quit()
    time.sleep(4)
