import pytest
from pom_elements.multi_element import MultiElement

pytestmark = pytest.mark.integration


def test_multi_element(selenium_chrome):
    """Verify that the MultiElement class can be used."""
    selenium_chrome.get("https://xkcd.com/")
    multi_elem = MultiElement(
        webdriver=selenium_chrome, timeout=0.5, xpath='//a[@href="/archive"]'
    )
    assert multi_elem.is_visible()


def test_multi_element_no_locator(selenium_chrome):
    """Verify that not setting any locators raises an error."""
    with pytest.raises(AttributeError):
        MultiElement(webdriver=selenium_chrome, timeout=0.5)


def test_multi_element_more_than_one_locator(selenium_chrome):
    """Verify that setting too many locators on a MultiElement raises an error."""
    with pytest.raises(AttributeError):
        MultiElement(webdriver=selenium_chrome, timeout=0.5, xpath="//div", css="a > p")


def test_set_locator_on_multi_element(selenium_chrome):
    """Verify that we can set a locator on a MultiElement."""
    multi_elem = MultiElement(
        webdriver=selenium_chrome, timeout=0.5, xpath='//a[@href="/archive"]'
    )
    with pytest.raises(NotImplementedError):
        multi_elem.locator = "css"
