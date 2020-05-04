import pytest
from pom_elements.xpath_element import XPathElement

pytestmark = pytest.mark.integration


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
