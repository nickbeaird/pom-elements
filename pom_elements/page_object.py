from selenium import webdriver


class PageObject:
    """The PageObject pattern allows for abstracting web pages into sections.

    Read more on the PageObject pattern as described by Martin Fowler https://martinfowler.com/bliki/PageObject.html.
    """

    def __init__(self, webdriver: webdriver = None, url: str = None) -> None:
        self.webdriver = webdriver
        self.url = url

    def __get__(self, instance, owner):
        """Return a PageObject and set the webdriver to the webdriver of the parent PageObject.

        The PageObject class should allow users to create a container of a concept for
        a Page, section, or widget of the web page. The user should also only have to set
        the webdriver for the page once, and have the webdriver be propogated through all
        instances that were assigned as variables to this instance.

        Additionally, we are propogating instance variables rather than using class
        variables as this allows us to set Pages with differing webdrivers. For example,
        one test can verify a PageObject with a WebDriver.session_id for Chrome, while
        a similar but separate instance creates a PageObject with a WebDriver.session_id
        for Firefox, Safari, or any other browser as available with Selenium.
        """
        instance_webdriver = getattr(instance, "webdriver", None)
        if instance_webdriver is not None:
            self.webdriver = instance_webdriver
        owner_webdriver = getattr(owner, "webdriver", None)
        print("instance_webdriver: ", instance_webdriver)
        print("owner_webdriver: ", owner_webdriver)
        return self
