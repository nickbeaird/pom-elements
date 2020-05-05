import pytest
from pom_elements.page_object import PageObject
from selenium import webdriver

# Set marker
pytestmark = pytest.mark.integration


# @pytest.mark.skip(
#     reason="Safari continues to be a pain on local setup. This test is overkill."
# )
def test_multiple_webdrivers_and_pageobject_sessions():
    """Test that a user can have many nested PageObject models and multiple WebDriver sessions.

    One of the largest use cases around creating a PageObject model is the ability to
    create multiple session ids. The thought is that each PageObject instance is able to
    have it's own instantiated instance, which allows us to spin up multiple browser
    instances. This is the main use case for not propogating a WebDriver instance to
    it's variable PageObjects via a class variable.

    Asserts that the multiple PageObjects can exist with their own WebDriver instance.
    """
    chrome = webdriver.Chrome()
    firefox = webdriver.Firefox()
    safari = webdriver.Safari()

    class Widget(PageObject):
        widget1 = PageObject()
        widget2 = PageObject()
        widget3 = PageObject()

    class Container(PageObject):
        container1 = Widget()
        container2 = Widget()
        container3 = Widget()

    class Page(PageObject):
        top = Container()
        middle = Container()
        bottom = Container()

    page_chrome = Page(webdriver=chrome)
    page_firefox = Page(webdriver=firefox)
    page_safari = Page(webdriver=safari)

    # Get the Webdriver.session_id all PageObject Chrome instances.
    chrome_page_session = page_chrome.webdriver.session_id
    chrome_top_tree_widget = page_chrome.top.container1.widget1.webdriver.session_id
    chrome_bottom_tree_widget = (
        page_chrome.bottom.container3.widget3.webdriver.session_id
    )

    # Get the Webdriver.session_id all PageObject Firefox instances.
    firefox_page_session = page_firefox.webdriver.session_id
    firefox_top_tree_widget = page_firefox.top.container1.widget1.webdriver.session_id
    firefox_bottom_tree_widget = (
        page_firefox.bottom.container3.widget3.webdriver.session_id
    )

    # Get the Webdriver.session_id all PageObject Safari instances.
    safari_page_session = page_safari.webdriver.session_id
    safari_top_tree_widget = page_safari.top.container1.widget1.webdriver.session_id
    safari_bottom_tree_widget = (
        page_safari.bottom.container3.widget3.webdriver.session_id
    )

    assert chrome_page_session == chrome_top_tree_widget == chrome_bottom_tree_widget
    assert firefox_page_session == firefox_top_tree_widget == firefox_bottom_tree_widget
    assert safari_page_session == safari_top_tree_widget == safari_bottom_tree_widget

    assert chrome_page_session != firefox_page_session

    chrome.quit()
    firefox.quit()
    safari.quit()
