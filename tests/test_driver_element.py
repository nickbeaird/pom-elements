import pytest
from pom_element.base_tag import BaseTag
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement


def test_get_web_element():
    """Test that the Tag class can return an element on instantiation."""
    browser = webdriver.Chrome()
    browser.get("https://www.google.com")
    elem = BaseTag(xpath="//input", type="text", webdriver=browser).find()
    assert isinstance(elem, WebElement)
    browser.quit()


def test_elem_is_visible():
    """Test that that the method is_visible() returns a boolean."""
    browser = webdriver.Chrome()
    browser.get("https://www.google.com")
    elem = BaseTag(xpath="//input", type="text", webdriver=browser)
    assert elem.is_visible() is True
    browser.quit()


def test_elem_can_be_clicked():
    """Test that an element can be checked to see if it can be clicked."""
    browser = webdriver.Chrome()
    browser.get("https://www.google.com")
    elem = BaseTag(xpath="//input", type="text", webdriver=browser)
    assert elem.can_be_clicked()
    browser.quit()


def test_click_elem():
    """Test that we can click a Selenium WebElement."""
    browser = webdriver.Chrome()
    browser.get("https://www.google.com")
    elem = BaseTag(xpath="//input", type="text", webdriver=browser)
    elem.click()
    browser.quit()


def test_elem_that_does_exist_raises_error():
    """Test that an element that cannot be found returns the correct error."""
    browser = webdriver.Chrome()
    browser.get("https://www.google.com")
    with pytest.raises(AssertionError):
        BaseTag(xpath="//input", type="flabber", webdriver=browser)
    browser.quit()


def test_can_set_timeout():
    """Test that a user can set a timeout on element."""
    browser = webdriver.Chrome()
    browser.get("https://www.google.com")
    with pytest.raises(AssertionError):
        BaseTag(xpath="//input", type="flabber", webdriver=browser, timeout=8)
    browser.quit()


def test_set_no_webdriver():
    """Test that a user receives an Attribute when a WebDriver is not set."""
    browser = webdriver.Chrome()
    browser.get("https://www.google.com")
    with pytest.raises(AttributeError):
        elem = BaseTag(xpath="//input", type="text")
        elem.click()
    browser.quit()
