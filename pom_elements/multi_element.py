from typing import Optional, Tuple, Union

from pom_elements.base_element import BaseElement
from selenium import webdriver
from selenium.webdriver.common.by import By


class MultiElement(BaseElement):
    """Set any Page Element using a Selenium Locators.

    Args:
        webdriver (webdriver): A selenium webdriver instance.
        timeout (float): An integer or float. Defaults to default timeout if not set.
    """

    LOCATOR = {
        "css": By.CSS_SELECTOR,
        "id_": By.ID,
        "name": By.NAME,
        "class_name": By.CLASS_NAME,
        "link_text": By.LINK_TEXT,
        "partial_link_text": By.PARTIAL_LINK_TEXT,
        "tag_name": By.TAG_NAME,
        "xpath": By.XPATH,
    }
    """The dictionary containing the Selenium LOCATOR reference."""

    def __init__(
        self, webdriver: webdriver = None, timeout: Optional[float] = 0.5, **kwargs
    ) -> None:
        locators = {k: v for k, v in kwargs.items() if k in self.LOCATOR}
        if len(locators) == 0 or kwargs is None:
            raise AttributeError("No attribute was set. Please set a Locator.")
        if len(locators) > 1:
            raise AttributeError(
                "Two attributes set and this can only set a single Locator."
            )
        k, v = next(iter(locators.items()))
        self._locator = (self.LOCATOR[k], v)
        super().__init__(webdriver, timeout)

    @property
    def locator(self) -> Tuple[By, str]:
        """Return the locator set on the class."""
        return self._locator

    @locator.setter
    def locator(self, locator: Union[Tuple[str, str], str]) -> None:
        """Set the locator for the class."""
        raise NotImplementedError(
            "Changing an Element's locator is not avilable at this time."
        )
