import pytest
from pom_elements.xpath_element import XPathElement
from selenium.webdriver.remote.webelement import WebElement

pytestmark = pytest.mark.integration


def test_get_web_element(selenium_chrome):
    """Test that the Tag class can return an element on instantiation."""
    selenium_chrome.get("https://www.google.com")
    elem = XPathElement(xpath="//input", type="text", webdriver=selenium_chrome).find()
    assert isinstance(elem, WebElement)


def test_elem_is_visible(selenium_chrome):
    """Test that that the method is_visible() returns a boolean."""
    selenium_chrome.get("https://www.google.com")
    elem = XPathElement(xpath="//input", type="text", webdriver=selenium_chrome)
    assert elem.is_visible() is True


def test_elem_can_be_clicked(selenium_chrome):
    """Test that an element can be checked to see if it can be clicked."""
    selenium_chrome.get("https://www.google.com")
    elem = XPathElement(xpath="//input", type="text", webdriver=selenium_chrome)
    assert elem.can_be_clicked()


def test_click_elem(selenium_chrome):
    """Test that we can click a Selenium WebElement."""
    selenium_chrome.get("https://www.google.com")
    elem = XPathElement(xpath="//input", type="text", webdriver=selenium_chrome)
    elem.click()


def test_elem_that_does_exist_raises_error(selenium_chrome):
    """Test that an element that cannot be found returns the correct error."""
    selenium_chrome.get("https://www.google.com")
    with pytest.raises(AssertionError):
        XPathElement(xpath="//input", type="flabber", webdriver=selenium_chrome)


def test_can_set_timeout(selenium_chrome):
    """Test that a user can set a timeout on element."""
    selenium_chrome.get("https://www.google.com")
    with pytest.raises(AssertionError):
        XPathElement(
            xpath="//input", type="flabber", webdriver=selenium_chrome, timeout=8
        )


def test_set_no_webdriver(selenium_chrome):
    """Test that a user receives an Attribute Error when a WebDriver is not set."""
    selenium_chrome.get("https://www.google.com")
    with pytest.raises(AttributeError):
        elem = XPathElement(xpath="//input", type="text", timeout=0.2)
        elem.click()
