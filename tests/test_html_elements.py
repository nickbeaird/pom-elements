from pom_elements.html import (
    DD,
    DT,
    H1,
    H2,
    H3,
    H4,
    H5,
    H6,
    OL,
    UL,
    Div,
    Link,
    P,
    Quote,
)


def test_h1():
    """Verify that the H1 tag returns the accurate xpath."""
    elem = H1()
    assert elem.xpath == "//h1"


def test_h2():
    """Verify that the H2 tag returns the accurate xpath."""
    elem = H2()
    assert elem.xpath == "//h2"


def test_h3():
    """Verify that the H3 tag returns the accurate xpath."""
    elem = H3()
    assert elem.xpath == "//h3"


def test_h4():
    """Verify that the H4 tag returns the accurate xpath."""
    elem = H4()
    assert elem.xpath == "//h4"


def test_h5():
    """Verify that the H5 tag returns the accurate xpath."""
    elem = H5()
    assert elem.xpath == "//h5"


def test_h6():
    """Verify that the H6 tag returns the accurate xpath."""
    elem = H6()
    assert elem.xpath == "//h6"


def test_link():
    """Verify that the Link tag returns the accurate xpath."""
    elem = Link()
    assert elem.xpath == "//a"


def test_p():
    """Verify that the P tag returns the accurate xpath."""
    elem = P()
    assert elem.xpath == "//p"


def test_div():
    """Verify that the Div tag returns the accurate xpath."""
    elem = Div()
    assert elem.xpath == "//div"


def test_quote():
    """Verify that the Quote tag returns the accurate xpath."""
    elem = Quote()
    assert elem.xpath == "//blockquote"


def test_dt():
    """Verify that the DT tag returns the accurate xpath."""
    elem = DT()
    assert elem.xpath == "//dt"


def test_DD():
    """Verify that the DD tag returns the accurate xpath."""
    elem = DD()
    assert elem.xpath == "//dd"


def test_OL():
    """Verify that the OL tag returns the accurate xpath."""
    elem = OL()
    assert elem.xpath == "//ol"


def test_UL():
    """Verify that the UL tag returns the accurate xpath."""
    elem = UL()
    assert elem.xpath == "//ul"
