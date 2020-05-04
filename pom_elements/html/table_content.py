from pom_elements import XPathElement


class Caption(XPathElement):
    """Interact with the <caption> html elment."""

    tag = "caption"


class Col(XPathElement):
    """Interact with the <col> html elment."""

    tag = "col"


class ColGroup(XPathElement):
    """Interact with the <colgroup> html elment."""

    tag = "colgroup"


class Table(XPathElement):
    """Interact with the <table> html elment."""

    tag = "table"


class TableData(XPathElement):
    """Interact with the <td> html elment."""

    tag = "td"


class TableFooter(XPathElement):
    """Interact with the <tfoot> html elment."""

    tag = "tfoot"


class TableHead(XPathElement):
    """Interact with the <thead> html elment."""

    tag = "thead"


class TableHeader(XPathElement):
    """Interact with the <th> html elment."""

    tag = "th"


class TableRow(XPathElement):
    """Interact with the <tr> html elment."""

    tag = "tr"
