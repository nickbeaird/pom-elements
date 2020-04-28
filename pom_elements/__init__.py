"""The Python package `pom-elements` for making Page Object and extend page Elements.

`pom-elements` allows for creating Page Object Models for your testing needs and
extending the model to Elements on the Page. The project is currently only supporting
Selenium webdriver instance, but is intended to help test writers abstract testing
organization around web page development choices.

.. include:: ../documentation.md
"""

from .multi_element import MultiElement
from .page_object import Page, PageObject
from .xpath_element import XPathElement

__all__ = ["MultiElement", "XPathElement", "PageObject", "Page"]
