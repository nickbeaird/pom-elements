from typing import Tuple

from pom_elements.base_element import BaseElement
from selenium import webdriver
from selenium.webdriver.common.by import By


class MultiElement(BaseElement):
    """Set any Page Element using a Selenium Locators."""

    _LOCATOR_MAP = {
        "css": By.CSS_SELECTOR,
        "id_": By.ID,
        "name": By.NAME,
        "xpath": By.XPATH,
        "link_text": By.LINK_TEXT,
        "partial_link_text": By.PARTIAL_LINK_TEXT,
        "tag_name": By.TAG_NAME,
        "class_name": By.CLASS_NAME,
    }

    def __init__(
        self, webdriver: webdriver = None, timeout: float = 0.5, **kwargs
    ) -> None:
        if kwargs is None:
            raise AttributeError("No attribute was set. Please set a Locator.")
        if len(kwargs) > 1:
            raise AttributeError(
                "Two attributes set and this can only set a single Locator."
            )
        k, v = next(iter(kwargs.items()))
        self._locator = (self._LOCATOR_MAP[k], v)
        super().__init__(webdriver, timeout)

    @property
    def locator(self) -> Tuple[By, str]:
        """Return the locator element set on the class."""
        return self._locator

    @locator.setter
    def locator(self, locator: Tuple[By, str]) -> None:
        """Set the locator for the class."""
        self._locator = locator
