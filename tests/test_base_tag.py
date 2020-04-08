from selenium_xpath.base_tag import BaseTag


def test_base_tag_xpath():
    """Test BaseTag functionality returns the correct xpath as a property."""
    a = BaseTag(
        xpath="//br", html_class="new_class", html_id="old_id", time_attr="newtest"
    )
    assert a.xpath == '//br[@class="new_class"][@id="old_id"][@time_attr="newtest"]'

    b = BaseTag(html_class="new_class", html_id="old_id", time_attr="newtest")
    assert b.xpath == '//*[@class="new_class"][@id="old_id"][@time_attr="newtest"]'

    c = BaseTag()
    assert c.xpath == "//*"


# TODO: Verify that a user can manually reset xpath.
