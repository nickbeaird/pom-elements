from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium_xpath.base_tag import BaseTag


def test_user_can_set_webdriver_on_tag():
    """Test that a uesr can set a webdriver on a tag set as a Class variable."""
    browser = webdriver.Chrome()
    browser.get("https://xkcd.com/")

    class xkcd_link_menu:
        archive = BaseTag(webddriver=browser, xpath="//a", href="/archive")
        howto = BaseTag(webddriver=browser, xpath="//a", href="/how-to/")
        about = BaseTag(webddriver=browser, xpath="//a", href="/about")

    # Page that works
    page = xkcd_link_menu()
    # Verify that a page object returns a web element
    assert isinstance(page.about.find(), WebElement)
    browser.quit()


def test_user_can_set_webdriver_on_pageobject():
    """Test that a user can set a webdriver on a PageObject only and not set it on the Element."""
    browser = webdriver.Chrome()
    browser.get("https://xkcd.com/")

    class xkcd_link_menu_wo_webdriver:
        webdriver = browser
        archive = BaseTag(xpath="//a", href="/archive")
        howto = BaseTag(xpath="//a", href="/how-to/")
        about = BaseTag(xpath="//a", href="/about")

    page2 = xkcd_link_menu_wo_webdriver()
    assert isinstance(page2.about.find(), WebElement)
    browser.quit()
