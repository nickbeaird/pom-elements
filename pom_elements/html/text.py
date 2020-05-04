from pom_elements import XPathElement


class P(XPathElement):
    """Interact with <p> tags."""

    tag = "p"


class Div(XPathElement):
    """Interact with <div> tags."""

    tag = "div"


class Quote(XPathElement):
    """Interact with <blockquote> tags."""

    tag = "blockquote"


class DT(XPathElement):
    """Interact with <dt> tags."""

    tag = "dt"


class DD(XPathElement):
    """Interact with <dd> tags."""

    tag = "dd"


class OL(XPathElement):
    """Interact with <ol> tags."""

    tag = "ol"


class UL(XPathElement):
    """Interact with <ul> tags."""

    tag = "ul"
