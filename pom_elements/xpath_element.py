from typing import Optional, Tuple

from pom_elements.base_element import BaseElement
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class XPathElement(BaseElement):
    """Generate xpath query and return Selenium WebElements as Page Elements.

    Args:
        webdriver (webdriver): A Selenium webdriver instance.
        timeout (float): An integer or float setting the default timeout for all XPath methods.
        xpath (str): The xpath can be directly set, or is auto-generated by the tag class variable, and attrbutes provided.
        text (str): Searches the provded Element for text that contains this value.
        html_INPUT (str): Adds the arg with the html_ removed from this. Useful for class and id.
        INPUT_contains (str): Add an xpath query to search for attributes that contain the value listed.


    Examples:
        >>> print(XPath(html_id="foo").xpath)
        '//*[@id="foo"]'

        >>> print(XPath(xpath='//div/span', data-attrbite='bar', name='baz').xpath)
        '//div/span[@data-attribute="bar"][@name="baz"]'

        >>> print(XPath(class_contains="foo").xpath)
        '//*[contains(@class, "foo")]'
    """

    tag = "*"
    """tag class attribute is the xpath html tag (i.e. div, span, ul)."""

    def __init__(
        self, webdriver: webdriver = None, timeout: int = 5, xpath: str = "", **kwargs,
    ) -> None:
        self.user_input = kwargs
        self.xpath = xpath
        super().__init__(webdriver, timeout)

    @property
    def locator(self) -> Tuple[By, str]:
        """Return the Xpath Locator element."""
        return (By.XPATH, self.xpath)

    def find(self, timeout: Optional[float] = None) -> WebElement:
        """Return the Selenium WebElement in the provided timeout or raise an error.

        Args:
            timeout: The length of time that we expect a WebElement to be returned within.
            Defaults to the _default_timeout if not set.
        """
        if timeout is None:
            timeout = self.default_timeout

        try:
            wait = WebDriverWait(self.webdriver, timeout)
            elem = wait.until(EC.presence_of_element_located(self.locator))

        except TimeoutException as exc:
            raise AssertionError(
                f"Unable to find {str(self.__repr__())}, xpath: {self.xpath} in the {timeout} seconds."
            ) from exc

        self.web_element = elem
        return elem

    @property
    def xpath(self) -> str:
        """Get the xpath value as a string."""
        return self._xpath

    @xpath.setter
    def xpath(self, xpath: str) -> None:  # noqa: C901
        """Set the xpath value of the string as value.

        Args:
            xpath: The xpath of the page element.
        """
        if not isinstance(xpath, str):
            raise ValueError("xpath must be of type str")

        generated_xpath = ""
        if xpath != "":
            generated_xpath = xpath
        else:
            generated_xpath = f"//{self.tag}"

        # Parse self.user_input and calculate xpath based on values provided.
        for key in self.user_input.keys():
            if key.startswith("html_"):
                arg_strip_html = key[5:]
                generated_xpath += f'[@{arg_strip_html}="{self.user_input[key]}"]'
            elif key == "text":
                generated_xpath += f'[contains(text(), "{self.user_input[key]}")]'
            elif key.endswith("_contains"):
                arg_in_xpath_args = key[:-9]
                generated_xpath += (
                    f'[contains(@{arg_in_xpath_args}, "{self.user_input[key]}")]'
                )
            else:
                generated_xpath += f'[@{key}="{self.user_input[key]}"]'
        self._xpath = generated_xpath

    def __repr__(self) -> str:
        """Return __repr__ of XPathElement."""
        return f'{self.__class__.__name__}(xpath="{str(self.xpath)}")'
