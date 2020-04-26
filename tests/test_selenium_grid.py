import pytest
from pom_elements.page_object import PageObject
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


@pytest.mark.skip(
    reason="Currently not a stable test due to Selenium Grid/Node connectivity."
)
def test_selenium_grid():
    """Verify that a user can use our project with Selenium Grid.

    This is not testing the PageObject methodology at scale, but is a proof of concept
    to make sure that we are not missing a common Selenium implementation.

    Todo:
        - Resolve Selenium Grid setup, so that it is easier to verify that this works.
        The connection to Selenium Grid is flakey, and there seems to be a lot of
        discussion online about the need to verify connection from the container before
        running the tests.

    Asserts that the session id is equivalant throughout the PageObjects.
    """
    chrome = webdriver.Remote(
        command_executor="http://0.0.0.0:4444/wd/hub",
        desired_capabilities=DesiredCapabilities.CHROME,
    )
    chrome.get("https://www.google.com/")
    assert chrome.title == "Google"

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

    page = Page(webdriver=chrome)

    # Get the Webdriver.session_id all PageObject instances.
    page_session = page.webdriver.session_id
    top_tree_widget = page.top.container1.widget1.webdriver.session_id
    bottom_tree_widget = page.bottom.container3.widget3.webdriver.session_id

    assert page_session == top_tree_widget == bottom_tree_widget

    chrome.quit()
