from pom_element.base_tag import BaseTag


def test_base_tag_xpath():
    """Test BaseTag functionality returns the correct xpath as a property."""
    a = BaseTag(
        xpath="//br", html_class="new_class", html_id="old_id", time_attr="newtest"
    )
    assert a.xpath == '//br[@class="new_class"][@id="old_id"][@time_attr="newtest"]'

    c = BaseTag()
    assert c.xpath == "//*"


def test_class_set_xpath():
    """Verify that the class variable is being set in the xpath and repr."""
    tag_with_class_set = BaseTag(html_class="new_class")
    assert tag_with_class_set.xpath == '//*[@class="new_class"]'

    assert str(tag_with_class_set) == 'BaseTag(xpath="//*[@class="new_class"]")'


def test_class_str_method():
    """Test that the correct __repr__ is being generated."""
    base_str = BaseTag()
    assert str(base_str) == 'BaseTag(xpath="//*")'
