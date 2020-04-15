"""POM-Elements allows provides for designing tests in an easy Page Object design pattern."""

from .multi_element import MultiElement
from .xpath_element import XPathElement

__all__ = ["MultiElement", "XPathElement"]
