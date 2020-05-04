from pom_elements import XPathElement


class Link(XPathElement):
    """Interact with <a> tags."""

    tag = "a"


class Cite(XPathElement):
    """Interact with <cite> tags."""

    tag = "cite"


class Code(XPathElement):
    """Interact with <code> tags."""

    tag = "code"


class Highlight(XPathElement):
    """Interact with <mark> tags."""

    tag = "mark"


class InlineQuote(XPathElement):
    """Interact with <q> tags."""

    tag = "q"


class Span(XPathElement):
    """Interact with <span> tags."""

    tag = "span"


class Subscript(XPathElement):
    """Interact with <sub> tags."""

    tag = "sub"


class Superscript(XPathElement):
    """Interact with <sup> tags."""

    tag = "sup"
