from pom_elements.page_object import PageObject
from pom_elements.xpath_element import XPathElement
from selenium.webdriver.remote.webelement import WebElement


def test_user_can_set_webdriver_on_tag(selenium_chrome):
    """Test that a uesr can set a webdriver on a tag set as a Class variable.

    We are verifying the base use case where someone wants to organize their tests by a
    rough page object model. We are verifying that a user can access the XPathElement instance
    as a set class variable on the page-like class.
    """
    selenium_chrome.get("https://xkcd.com/")

    class xkcd_link_menu:
        archive = XPathElement(webdriver=selenium_chrome, xpath="//a", href="/archive")
        howto = XPathElement(webdriver=selenium_chrome, xpath="//a", href="/how-to/")
        about = XPathElement(webdriver=selenium_chrome, xpath="//a", href="/about")

    # Page that works
    page = xkcd_link_menu()
    # Verify that a page object returns a web element
    assert isinstance(page.about.find(), WebElement)


def test_user_can_set_webdriver_on_pageobject(selenium_chrome):
    """Test that a user can set a webdriver on a PageObject only and not set it on the Element.

    We are inferring that the user is able to propogate the webdriver instance to the
    XPathElement instance by the virtue that the XPathElement is able to instantiate, allow the
    browser to run, and then click then find and return and instance of WebElement.
    """
    selenium_chrome.get("https://xkcd.com/")

    class xkcd_link_menu_wo_webdriver:
        webdriver = selenium_chrome
        archive = XPathElement(xpath="//a", href="/archive")
        howto = XPathElement(xpath="//a", href="/how-to/")
        about = XPathElement(xpath="//a", href="/about")

    page2 = xkcd_link_menu_wo_webdriver()
    assert isinstance(page2.about.find(), WebElement)


def test_nested_pageobject_two_deep(selenium_chrome):
    """Test that a user can have nested PageObject models.

    This test verifies that a user is able to create a PageObject, and then add any
    number of PageObjects to the page without worrying about setting the WebDriver on
    each successive class. The thought here is that the user can create any number of
    widgets with a PageObject and pull them into any number of pages.

    Asserts that the session id is equivalant throughout the PageObjects.
    """

    class xkcd_link_menu(PageObject):
        pass

    class main_page(PageObject):
        header = PageObject()
        menu = xkcd_link_menu()
        footer = PageObject()

    page3 = main_page(webdriver=selenium_chrome)

    # Get the Webdriver.session_id all PageObject instances.
    page3_session_id = page3.webdriver.session_id
    page3header_session_id = page3.header.webdriver.session_id
    page3menu_session_id = page3.menu.webdriver.session_id
    page3footer_session_id = page3.footer.webdriver.session_id

    assert (
        page3_session_id
        == page3header_session_id
        == page3menu_session_id
        == page3footer_session_id
    )


# @pytest.mark.skip(
#     reason="This test is working and is a little heavy for fast development."
# )


def test_nested_pageobject_multiple_deep(selenium_chrome):
    """Test that a user can have many nested PageObject models.

    This test verifies that a user is able to create a PageObject, and then add any
    number of PageObjects to the page without worrying about setting the WebDriver on
    each successive class. The thought here is that the user can create any number of
    widgets with a PageObject and pull them into any number of pages.

    Asserts that the session id is equivalant throughout the PageObjects.
    """

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

    page = Page(webdriver=selenium_chrome)

    # Get the Webdriver.session_id all PageObject instances.
    page_session = page.webdriver.session_id
    top_tree_widget = page.top.container1.widget1.webdriver.session_id
    bottom_tree_widget = page.bottom.container3.widget3.webdriver.session_id

    assert page_session == top_tree_widget == bottom_tree_widget


def test_page_object(selenium_chrome):
    """How does this work."""
    selenium_chrome.get("https://xkcd.com/")

    class Menu(PageObject):
        archive_link = XPathElement(xpath="//a", href="/archive")
        how_to = XPathElement(xpath="//a", href="/how-to/")

    class XKCDMainPage(PageObject):
        menu = Menu()

    page = XKCDMainPage(webdriver=selenium_chrome)
    assert page.menu.how_to.can_be_clicked()
    assert page.menu.how_to.xpath == '//a[@href="/how-to/"]'
