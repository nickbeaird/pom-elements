from pom_elements.html import (
    Cite,
    Code,
    Highlight,
    InlineQuote,
    Link,
    Span,
    Subscript,
    Superscript,
)


def test_html_inline_text_element_Link():
    """Verify that the Link Element returns the xpath to select this html dom element."""
    elem = Link()
    assert elem.xpath == "//a"


def test_html_inline_text_element_Cite():
    """Verify that the cite Element returns the xpath to select this html dom element."""
    elem = Cite()
    assert elem.xpath == "//cite"


def test_html_inline_text_element_Code():
    """Verify that the Code Element returns the xpath to select this html dom element."""
    elem = Code()
    assert elem.xpath == "//code"


def test_html_inline_text_element_Highlight():
    """Verify that the Highlight Element returns the xpath to select this html dom element."""
    elem = Highlight()
    assert elem.xpath == "//mark"


def test_html_inline_text_element_InlineQuote():
    """Verify that the InlineQuote Element returns the xpath to select this html dom element."""
    elem = InlineQuote()
    assert elem.xpath == "//q"


def test_html_inline_text_element_Span():
    """Verify that the Span Element returns the xpath to select this html dom element."""
    elem = Span()
    assert elem.xpath == "//span"


def test_html_inline_text_element_Subscript():
    """Verify that the Subscript Element returns the xpath to select this html dom element."""
    elem = Subscript()
    assert elem.xpath == "//sub"


def test_html_inline_text_element_Superscript():
    """Verify that the Superscript Element returns the xpath to select this html dom element."""
    elem = Superscript()
    assert elem.xpath == "//sup"
