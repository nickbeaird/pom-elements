from pathlib import Path

import pytest
from pom_elements.xpath_element import XPathElement


def get_filename(filename: str) -> str:
    """Returns the path of the filename provided in the test directory."""
    path = Path.cwd() / "tests" / filename
    return "file://" + str(path)


def test_xpath_elem():
    """Test XPathElement functionality returns the correct xpath as a property."""
    a = XPathElement(
        xpath="//br", html_class="new_class", html_id="old_id", time_attr="newtest"
    )

    assert a.xpath == '//br[@class="new_class"][@id="old_id"][@time_attr="newtest"]'

    c = XPathElement()
    assert c.xpath == "//*"


def test_class_set_xpath_elem():
    """Verify that the class variable is being set in the xpath and repr."""
    tag_with_class_set = XPathElement(html_class="new_class")
    assert tag_with_class_set.xpath == '//*[@class="new_class"]'
    assert str(tag_with_class_set) == 'XPathElement(xpath="//*[@class="new_class"]")'


def test_class_str_method_xpath_elem():
    """Test that the correct __repr__ is being generated."""
    base_str = XPathElement()
    assert str(base_str) == 'XPathElement(xpath="//*")'


def test_xpath_val_cannot_be_int():
    """Verfiy that a user cannot set any xpath values taht are not of type str."""
    with pytest.raises(ValueError):
        XPathElement(xpath=1)


def test_xpath_text():
    """Verify that a user can select a specific type of text."""
    elem = XPathElement(text="This is a test")
    assert elem.xpath == '//*[contains(text(), "This is a test")]'


@pytest.mark.integration
def test_xpath_text_selection(selenium_chrome):
    """Verify that a webdriver instance can select a tag that has a specific text value."""
    file_location = get_filename("test_xpath.html")
    selenium_chrome.get(file_location)
    elem = XPathElement(webdriver=selenium_chrome, xpath="//h1", text="Selenium Test")
    elem.is_visible()


def test_xpath_attr_contains():
    """Verify that a user can select a limited section of values of attributes.

    This is often useful when wanting to select an attribute that has many data values,
    or many class attributes compiled together.
    """
    elem = XPathElement(class_contains="red")
    assert elem.xpath == '//*[contains(@class, "red")]'


@pytest.mark.integration
def test_class_contains(selenium_chrome):
    """Verify that selenium can find an element that contains one attribute if there are many."""
    file_location = get_filename("test_xpath.html")
    selenium_chrome.get(file_location)
    elem = XPathElement(webdriver=selenium_chrome, xpath="//p", class_contains="red")
    elem.is_visible()
