from abc import ABC, abstractmethod

from pom_elements.harness import Harness
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BaseElement(ABC):
    """Abstract Base class to set most Element commands."""

    def __init__(self, webdriver=None, timeout=0.5):
        self._default_timeout = timeout
        if webdriver:
            self._webdriver = webdriver
            self.web_element = self.find()

    @property
    @abstractmethod
    def locator(self):
        """Return the Selenium locator used for this object."""
        raise NotImplementedError(
            "Any class that inherits from this needs to have a locator set."
        )

    def find(self, timeout: int = None) -> WebElement:
        """Return the Selenium WebElement in the provided timeout, or raise an error."""
        if timeout is None:
            timeout = self.default_timeout

        try:
            wait = WebDriverWait(self.webdriver, timeout)
            elem = wait.until(EC.presence_of_element_located(self.locator))

        except TimeoutException as exc:
            raise AssertionError(
                f"Unable to find {str(self.__repr__())} in the {timeout} seconds."
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

    def click(self, timeout: int = None):
        """Click the web element if it is available to be clicked."""
        if timeout is None:
            timeout = self.default_timeout

        self.find(timeout=timeout)
        self.web_element.click()

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
