"""The Python package `pom-elements.html` module is for interacting with html Elements.

`pom-elements.html` extends the XPathElement class to improve the `pom-elements`
experience writing tests for DOM elements. Refer to the Mozilla HTML Elements reference
documentation. https://developer.mozilla.org/en-US/docs/Web/HTML/Element
"""
from .content import H1, H2, H3, H4, H5, H6
from .inline_text import (
    Cite,
    Code,
    Highlight,
    InlineQuote,
    Link,
    Span,
    Subscript,
    Superscript,
)
from .media_and_embedded import Area, Iframe, Img, Picture, Source, Video
from .table_content import (
    Caption,
    Col,
    ColGroup,
    Table,
    TableData,
    TableFooter,
    TableHead,
    TableHeader,
    TableRow,
)
from .text import DD, DT, OL, UL, Div, P, Quote

__all__ = [
    "H1",
    "H2",
    "H3",
    "H4",
    "H5",
    "H6",
    "Link",
    "P",
    "Div",
    "Quote",
    "DT",
    "DD",
    "OL",
    "UL",
    "Link",
    "Cite",
    "Code",
    "Highlight",
    "InlineQuote",
    "Span",
    "Subscript",
    "Superscript",
    "Area",
    "Img",
    "Video",
    "Iframe",
    "Picture",
    "Source",
    "Caption",
    "Col",
    "ColGroup",
    "Table",
    "TableData",
    "TableFooter",
    "TableHead",
    "TableHeader",
    "TableRow",
]
