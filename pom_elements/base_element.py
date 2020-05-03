from abc import ABC, abstractmethod
from typing import Any, Optional

from pom_elements._harness import Harness
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BaseElement(ABC):
    """Base Element is an Abstract Base Class sets all methods for all inherited Element classes.

    This class must be inherited and the `locator` method needs to be defined.

    Args:
        webdriver (webdriver): A selenium webdriver instance (i.e. webdriver.Chrome(), webdriver.Firefox(), etc.)
        timeout (float): An integer or float setting the default timeout for all BaseElement methods.
    """

    def __init__(self, webdriver: webdriver = None, timeout: Optional[float] = 0.5):
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

    def find(self, timeout: Optional[float] = None) -> WebElement:
        """Returns the defined Selenium WebElement in the provided timeout or raise an error.

        Args:
            timeout: The length of time that we expect a WebElement to be returned within. Defaults
            to the _default_timeout if not set.

        Raises:
            AssertionError: Asserts that an element should be visible within the specified timeout.

        Returns:
            WebElement: A Selenium Webelement
        """
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

    def is_visible(self, timeout: Optional[int] = None) -> bool:
        """Return true if the webelement is visible on the page in the time (seconds) provided.

        Args:
            timeout: The length of time that we expect a WebElement to be returned within. Defaults
            to the _default_timeout if not set.

        Returns:
            bool: True if element is visible.
        """
        if timeout is None:
            timeout = self.default_timeout

        is_visible = WebDriverWait(self.webdriver, timeout).until(
            EC.visibility_of(self.web_element)
        )
        if is_visible:
            return True
        return False

    def is_invisible(self, timeout: Optional[int] = None) -> bool:
        """Return true if the webelement is invisible on the page within the time (seconds) provided.

        Args:
            timeout: The length of time that we expect the WebElement to return that it
            is in visible. Defaults to the _default_timeout if not set.

        Returns:
            bool: True if element is visible.
        """
        if timeout is None:
            timeout = self.default_timeout

        is_visible = WebDriverWait(self.webdriver, timeout).until(
            EC.invisibility_of_element(self.locator)
        )
        if is_visible:
            return True
        return False

    def can_be_clicked(self, timeout: Optional[int] = None) -> bool:
        """Return true if the webelement can be clicked in the time (seconds) provided.

        Args:
            timeout: The length of time that we expect a WebElement to be returned within. Defaults to the _default_timeout if not set.

        Returns:
            bool: True if element can be clicked.
        """
        if timeout is None:
            timeout = self.default_timeout

        # The method returns an webelement if true and false otherwise. We ignore the
        # found Selenium WebElement as we already have this item stored.
        is_clickable = WebDriverWait(self.webdriver, timeout).until(
            EC.element_to_be_clickable(self.locator)
        )
        if is_clickable is False:
            return False
        return True

    @property
    def webdriver(self) -> webdriver:
        """Get the Element's Selenium webdriver instance.

        Returns:
            WebElement: A Selenium Webelement
        """
        try:
            return self._webdriver
        except AttributeError as exc:
            raise AttributeError(
                "A webdriver instance needs to be set on the Tag or the PageObject class."
            ) from exc

    @webdriver.setter
    def webdriver(self, wd: webdriver) -> None:
        """Set the Element's Selenium webdriver instance.

        Args:
            wd: Selenium webdriver instance.
        """
        self._webdriver = wd

    @property
    def default_timeout(self):
        """Get the default timeout."""
        return self._default_timeout

    @default_timeout.setter
    def default_timeout(self, timeout: Optional[float] = None) -> None:
        """Set the default timeout for all methods.

        Args:
            timeout: The length of time that we expect a WebElement to be returned within. Sets the default timeout for all methods on the instance.
        """
        if timeout is None:
            timeout = Harness.global_timeout
        self._default_timeout = timeout

    def click(self, timeout: Optional[float] = None):
        """Click the web element if it is available to be clicked."""
        if timeout is None:
            timeout = self.default_timeout

        self.find(timeout=timeout)
        self.web_element.click()

    def is_displayed(self):
        """Returns true if the Element is displayed else false."""
        is_displayed = self.webdriver.is_displayed()
        if is_displayed:
            return True
        return False

    def get_attribute(self, name):
        """Returns the attribute of the name provided."""
        return self.webdriver.get_attribute(name)

    def get_all_attributes(self) -> dict:
        """Return a dictionary containing all of the attributes of an element."""
        if not self.webdriver.execute_script:
            raise AttributeError(
                "This webdriver type does not have this ability at this time."
            )
        return self.webdriver.execute_script(
            "var items = {}; for (index = 0; index < arguments[0].attributes.length; ++index) { items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value }; return items;",
            self.web_element,
        )

    def get_property(self, value: str) -> Any:
        """Get the property of the element.

        Args:
            property - Name of the property to retrieve.

        Returns:
            The property of the provided name.
        """
        return self.webdriver.get_property(value)

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
