"""POM-Elements allows for creating Page Object and adding Page Elements (MultiElement, XPathElement)."""

from .multi_element import MultiElement
from .xpath_element import XPathElement

__all__ = ["MultiElement", "XPathElement"]
