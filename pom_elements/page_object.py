from selenium import webdriver


class PageObject:
    """Class that allows for easily outlining your web pages as classes.

    Todo:
        Add type hints for the Selenium library to add Optional[webdriver].

    Args:
        webdriver (webdriver): A selenium webdriver instance for the PageObject.
    """

    def __init__(self, webdriver: webdriver = None) -> None:
        if webdriver is not None:
            self.webdriver = webdriver

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


class Page(PageObject):
    """The class representing all of the methods and interactions of a web page.

    A Page represents all of the functionality of the webdriver that is not encapsulated
    in the PageElement objects. The attached methods are all interactions with the web
    browser instance, and not elements on a single web page.

    Args:
        webdriver (webdriver): A selenium webdriver instance for the PageObject.
        url (str): The url of the the PageObject.
    """

    def __init__(self, webdriver: webdriver, url: str) -> None:
        super().__init__(webdriver=webdriver)
        self._url = url

    @property
    def url(self) -> str:
        """Get the url defined for this Page Object."""
        return self._url

    @url.setter
    def url(self, url: str) -> None:
        """Set the url for this instance.

        Args:
            url: The url that this Page should be defined.
        """
        self._url = url

    @property
    def current_url(self) -> str:
        """Return the url of the page currently being displayed by the webdriver."""
        return self.webdriver.current_url

    def go(self) -> None:
        """Navigate to the url set as the url for this Page object."""
        self.webdriver.get(self.url)

    def get(self, url: str) -> None:
        """Navigate to the provided url.

        Args:
            url: A url as a string.
        """
        self.webdriver.get(url)

    def back(self) -> None:
        """Navigate back one page on the web browser."""
        self.webdriver.back()

    def forward(self) -> None:
        """Navigate forward one page on the web browser."""
        self.webdriver.forward()

    def refresh(self) -> None:
        """Refresh the web browser."""
        self.webdriver.refresh()

    @property
    def title(self) -> str:
        """The title of the current web page."""
        return self.webdriver.title

    def quit(self) -> None:
        """Quit the webdriver instance."""
        self.webdriver.quit()

    def maximize_window(self) -> None:
        """Maximize the web browser's window."""
        self.webdriver.maximize_window()

    def minimize_window(self) -> None:
        """Minimize the web browser's window."""
        self.webdriver.minimize_window()
