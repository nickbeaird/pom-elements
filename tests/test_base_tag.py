from pom_elements.xpath_element import XPathElement


def test_base_tag_xpath():
    """Test XPathElement functionality returns the correct xpath as a property."""
    a = XPathElement(
        xpath="//br", html_class="new_class", html_id="old_id", time_attr="newtest"
    )
    import pdb

    pdb.set_trace()
    assert a.xpath == '//br[@class="new_class"][@id="old_id"][@time_attr="newtest"]'

    c = XPathElement()
    assert c.xpath == "//*"


def test_class_set_xpath():
    """Verify that the class variable is being set in the xpath and repr."""
    tag_with_class_set = XPathElement(html_class="new_class")
    assert tag_with_class_set.xpath == '//*[@class="new_class"]'

    assert str(tag_with_class_set) == 'XPathElement(xpath="//*[@class="new_class"]")'


def test_class_str_method():
    """Test that the correct __repr__ is being generated."""
    base_str = XPathElement()
    assert str(base_str) == 'XPathElement(xpath="//*")'
