from pom_element.base_tag import MultiElement
from selenium import webdriver


def test_multi_element():
    """Verify that the MultiElement class can be used."""
    browser = webdriver.Chrome()
    browser.get("https://xkcd.com/")
    xpath = MultiElement(webdriver=browser, timeout=0.5, xpath='//a[@href="/archive"]')
    assert xpath.is_visible()
    browser.quit()
