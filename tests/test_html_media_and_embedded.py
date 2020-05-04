from pom_elements.html import Area, Iframe, Img, Picture, Source, Video


def test_html_media_Area():
    """Verify that the Area class returns the accurate xpath."""
    elem = Area()
    assert elem.xpath == "//area"


def test_html_media_Img():
    """Verify that the Img class returns the accurate xpath."""
    elem = Img()
    assert elem.xpath == "//img"


def test_html_media_Video():
    """Verify that the Video class returns the accurate xpath."""
    elem = Video()
    assert elem.xpath == "//video"


def test_html_media_Iframe():
    """Verify that the Iframe class returns the accurate xpath."""
    elem = Iframe()
    assert elem.xpath == "//iframe"


def test_html_media_Picture():
    """Verify that the Picture class returns the accurate xpath."""
    elem = Picture()
    assert elem.xpath == "//picture"


def test_html_media_Source():
    """Verify that theSource class returns the accurate xpath."""
    elem = Source()
    assert elem.xpath == "//source"
