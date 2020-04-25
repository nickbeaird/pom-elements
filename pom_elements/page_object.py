from typing import Optional

from selenium import webdriver


class PageObject:
    """The PageObject allows for abstracting web pages into full pages or sections.

    Args:
        webdriver (webdriver): A selenium webdriver instance for the PageObject.
        url (str): The url of the the PageObject.
    """

    def __init__(self, webdriver: webdriver = None, url: Optional[str] = None) -> None:
        self.webdriver = webdriver
        self.url = url

    def __get__(self, instance, owner):
        """Return a PageObject and set the webdriver to the webdriver of the parent PageObject instance.

        The PageObject class allows users to create any number of PageObject instances
        as class variables on a PageObject class and pass the webdriver from parent
        PageObject class to itself.

        Additionally, we are propogating the webdriver as instance variables rather than
        class variables, as this allows us to create any number of PageObject instances
        under a single PageObject representing the Page and use separate webdrivers. For
        example, one test can verify a PageObject with a WebDriver.session_id for Chrome,
        while a separate instantiated PageObject Page can have a WebDriver.session_id
        for Firefox, Safari, or any other browser as available with Selenium.
        """
        instance_webdriver = getattr(instance, "webdriver", None)
        if instance_webdriver is not None:
            self.webdriver = instance_webdriver
        return self
