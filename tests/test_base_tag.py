from selenium_xpath.base_tag import BaseTag


def test_base_tag():
    """Test BaseTag functionality."""
    a = BaseTag("//br", html_class="new_class", html_id="old_id", time_attr="newtest")
    assert a.xpath == '//br[@class="new_class"][@id="old_id"][@time_attr="newtest"]'
