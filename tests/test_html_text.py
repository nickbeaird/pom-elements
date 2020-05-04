from pom_elements.html import DD, DT, OL, UL, Div, P, Quote


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
