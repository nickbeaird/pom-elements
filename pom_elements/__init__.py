"""The Python package `pom-elements` for a Page Object Model that extends to Page Elements.

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
__author__ = "Nick Beaird"
__author_email__ = "nicklasbeaird@gmail.com"
__license__ = "MIT"
__url__ = "https://github.com/nickbeaird/pom-elements"
__version__ = "0.1.1"
