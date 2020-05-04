from pom_elements.html import (
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


def test_html_table_element_Caption():
    """Verify that the Caption class returns the accurate xpath selectors."""
    elem = Caption()
    assert elem.xpath == "//caption"


def test_html_table_element_Col():
    """Verify that the Col class returns the accurate xpath selectors."""
    elem = Col()
    assert elem.xpath == "//col"


def test_html_table_element_ColGroup():
    """Verify that the ColGroup class returns the accurate xpath selectors."""
    elem = ColGroup()
    assert elem.xpath == "//colgroup"


def test_html_table_element_Table():
    """Verify that the Table class returns the accurate xpath selectors."""
    elem = Table()
    assert elem.xpath == "//table"


def test_html_table_element_TableData():
    """Verify that the TableData class returns the accurate xpath selectors."""
    elem = TableData()
    assert elem.xpath == "//td"


def test_html_table_element_TableFooter():
    """Verify that the TableFooter class returns the accurate xpath selectors."""
    elem = TableFooter()
    assert elem.xpath == "//tfoot"


def test_html_table_element_TableHead():
    """Verify that the TableHead class returns the accurate xpath selectors."""
    elem = TableHead()
    assert elem.xpath == "//thead"


def test_html_table_element_TableHeader():
    """Verify that the TableHeader class returns the accurate xpath selectors."""
    elem = TableHeader()
    assert elem.xpath == "//th"


def test_html_table_element_TableRow():
    """Verify that the TableRow class returns the accurate xpath selectors."""
    elem = TableRow()
    assert elem.xpath == "//tr"
