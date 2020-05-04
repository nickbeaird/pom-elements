from pom_elements.html import H1, H2, H3, H4, H5, H6


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
