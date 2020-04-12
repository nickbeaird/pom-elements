from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium_xpath.harness import Harness


class BaseTag:
    """Base tag to inherit all tags from."""

    tag = "*"
    css = ""

    def __init__(
        self, webdriver: webdriver = None, xpath: str = "", timeout: int = 5, **kwargs
    ) -> None:
        self.user_input = kwargs
        self.xpath = xpath
        self._default_timeout = timeout
        if webdriver:
            self._webdriver = webdriver
            self.web_element = self.find()

    @property
    def webdriver(self) -> webdriver:
        """Get the tag's Selenium webdriver instance."""
        try:
            return self._webdriver
        except AttributeError as exc:
            raise AttributeError(
                "A webdriver instance needs to be set on the Tag or the PageObject class."
            ) from exc

    @webdriver.setter
    def webdriver(self, wd) -> None:
        """Set the tag's Selenium webdriver instance."""
        self._webdriver = wd

    @property
    def default_timeout(self):
        """Get the default timeout."""
        return self._default_timeout

    @default_timeout.setter
    def default_timeout(self, timeout: int = None) -> None:
        """Set the default timeout."""
        if timeout is None:
            timeout = Harness.global_timeout
        self._default_timeout = timeout

    def find(self, timeout: int = None) -> WebElement:
        """Return the Selenium WebElement in the provided timeout, or raise an error."""
        if timeout is None:
            timeout = self.default_timeout

        try:
            wait = WebDriverWait(self.webdriver, timeout)
            elem = wait.until(EC.presence_of_element_located((By.XPATH, self.xpath)))

        except TimeoutException as exc:
            raise AssertionError(
                f"Unable to find {str(self.__repr__())}, xpath: {self.xpath} in the {timeout} seconds."
            ) from exc

        self.web_element = elem
        return elem

    def is_visible(self, timeout: int = None) -> bool:
        """Return true if the webelement is visible on the page in the time (seconds) provided."""
        if timeout is None:
            timeout = self.default_timeout

        is_visible = WebDriverWait(self.webdriver, timeout).until(
            EC.visibility_of(self.web_element)
        )
        if is_visible:
            return True
        return False

    def can_be_clicked(self, timeout: int = None) -> bool:
        """Return true if the webelement can be clicked in the time (seconds) provided."""
        if timeout is None:
            timeout = self.default_timeout

        # The method returns an webelement if true and false otherwise. We ignore the
        # found Selenium WebElement as we already have this item stored.
        is_clickable = WebDriverWait(self.webdriver, timeout).until(
            EC.visibility_of(self.web_element)
        )
        if is_clickable is False:
            return False
        return True

    def click(self, timeout: int = None):
        """Click the web element if it is available to be clicked."""
        if timeout is None:
            timeout = self.default_timeout

        self.find(timeout=timeout)
        self.web_element.click()

    @property
    def xpath(self) -> str:
        """Get the xpath value as a string."""
        return self._xpath

    @xpath.setter
    def xpath(self, xpath: str) -> None:
        """Set the xpath value of the string as value."""
        if not isinstance(xpath, str):
            raise ValueError("xpath must be of type str")

        generated_xpath = ""
        if xpath != "":
            generated_xpath = xpath
        else:
            generated_xpath = f"//{self.tag}"

        for key in self.user_input.keys():
            if key.startswith("html_"):
                new_value = key[5:]
                generated_xpath += f'[@{new_value}="{self.user_input[key]}"]'
            else:
                generated_xpath += f'[@{key}="{self.user_input[key]}"]'
        self._xpath = generated_xpath

    def __get__(self, instance, owner):
        """Update the __get__ method to set the webdriver and refresh the webelement.

        There are several areas that make this element object much more complicated. The
        class returns the class object as well as finding the Selenium WebElement on the
        page. More often than not errors arise when the page refreshes, or elements become
        stale. The user tries to interact with the selenim WebElement only to find out
        that it is not available. Overriding the __get__ method here allows us to refresh
        the WebElement every time the object is access.

        A second class of errors arises around allowing the user to set a Selenim WebDriver
        on the PageObject. The user has the ability to import and instantiate a single
        Element and set the element to have it's own WebDriver. However after working to
        abstract full pages, the user experience becomes numb if you have to add a webdriver
        to every Tag. To remedy this, we allow the user to set the Webdriver on the
        PageObject, and then the __get__ method here sets the webdriver to the webdriver
        found from the accessing instance.

        Allows setting a webdriver on the PageObject and refreshes the instance when accessed.
        """
        parent_webdriver = getattr(instance, "webdriver", None)
        if parent_webdriver is not None:
            self.webdriver = parent_webdriver
        self.find()
        return self

    def __repr__(self) -> str:
        """Return __repr__ of BaseTag."""
        return f"{self.__class__.__name__}(xpath='{str(self.xpath)}')"


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


# TODO: Remove when I am sure that we are not wanting to set session as a class variable.
# class PageObject:
#     def __init__(self, webdriver: webdriver = None, url: str = None) -> None:
#         PageObject.webdriver = webdriver
#         PageObject.url = url

#     def __get__(self, instance, owner):
#         return self
