import unittest

import pytest
from pom_elements.page_object import PageObject
from pom_elements.xpath_element import XPathElement
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement

pytestmark = pytest.mark.integration


class ChromeDriver(unittest.TestCase):
    """Setup class for unittest style unit tests."""

    def setUp(self):
        """Set a webdriver for all unitest style integration tests."""
        self.driver = webdriver.Chrome()

    def tearDown(self):
        """Tear down browser after tests complete."""
        self.driver.close()


class TestXPathElement(ChromeDriver):
    """Verify that Tags are able to be set with unittest class structure."""

    def test_can_use_XPathElement_with_webdriver(self):
        """Verify that unittest tests allow for setting the webdriver directly on the Tag."""
        self.driver.get("https://xkcd.com/")

        class xkcd_link_menu:
            """Test class for setting up a non-pageobject container for tag."""

            archive = XPathElement(webdriver=self.driver, xpath="//a", href="/archive")
            howto = XPathElement(webdriver=self.driver, xpath="//a", href="/how-to/")
            about = XPathElement(webdriver=self.driver, xpath="//a", href="/about")

        # Page that works
        page = xkcd_link_menu()
        # Verify that a page object returns a web element
        assert isinstance(page.about.find(), WebElement)

    def test_can_use_XPathElement_without_webdriver(self):
        """Verify that a user can instantiate a browser on all tags with a class variable."""
        self.driver.get("https://xkcd.com/")

        class xkcd_link_menu_wo_webdriver:
            """Class to set a webdriver on the class variable."""

            webdriver = self.driver
            archive = XPathElement(xpath="//a", href="/archive")
            howto = XPathElement(xpath="//a", href="/how-to/")
            about = XPathElement(xpath="//a", href="/about")

        page2 = xkcd_link_menu_wo_webdriver()
        assert isinstance(page2.about.find(), WebElement)


class TestPageObject(ChromeDriver):
    """Verify the PageObject used in unittest style tests."""

    def setUp(self):
        """Set a webdriver for all unitest style integration tests."""
        self.chrome = webdriver.Chrome()
        self.firefox = webdriver.Firefox()
        self.safari = webdriver.Safari()

    def tearDown(self):
        """Tear down browser after tests complete."""
        self.chrome.close()
        self.firefox.close()
        self.safari.close()

    @pytest.mark.skip(
        reason="Safari continues to be a pain on local setup. This test is not necessary."
    )
    def test_complex_pageobject_in_unittest(self):
        """Test that we can use unittest style tests with complex page object selenium sessions."""

        class Widget(PageObject):
            """A widget PageObject."""

            widget1 = PageObject()
            widget2 = PageObject()
            widget3 = PageObject()

        class Container(PageObject):
            """A Container PageObject."""

            container1 = Widget()
            container2 = Widget()
            container3 = Widget()

        class Page(PageObject):
            """A Page PageObject."""

            top = Container()
            middle = Container()
            bottom = Container()

        page_chrome = Page(webdriver=self.chrome)
        page_firefox = Page(webdriver=self.firefox)
        page_safari = Page(webdriver=self.safari)

        # Get the Webdriver.session_id all PageObject Chrome instances.
        chrome_page_session = page_chrome.webdriver.session_id
        chrome_top_tree_widget = page_chrome.top.container1.widget1.webdriver.session_id
        chrome_bottom_tree_widget = (
            page_chrome.bottom.container3.widget3.webdriver.session_id
        )

        # Get the Webdriver.session_id all PageObject Firefox instances.
        firefox_page_session = page_firefox.webdriver.session_id
        firefox_top_tree_widget = (
            page_firefox.top.container1.widget1.webdriver.session_id
        )
        firefox_bottom_tree_widget = (
            page_firefox.bottom.container3.widget3.webdriver.session_id
        )

        # Get the Webdriver.session_id all PageObject Safari instances.
        safari_page_session = page_safari.webdriver.session_id
        safari_top_tree_widget = page_safari.top.container1.widget1.webdriver.session_id
        safari_bottom_tree_widget = (
            page_safari.bottom.container3.widget3.webdriver.session_id
        )

        assert (
            chrome_page_session == chrome_top_tree_widget == chrome_bottom_tree_widget
        )
        assert (
            firefox_page_session
            == firefox_top_tree_widget
            == firefox_bottom_tree_widget
        )
        assert (
            safari_page_session == safari_top_tree_widget == safari_bottom_tree_widget
        )

        assert chrome_page_session != firefox_page_session
