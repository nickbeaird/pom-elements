from pom_elements import XPathElement


class Area(XPathElement):
    """Interact with <area> html tags."""

    tag = "area"


class Img(XPathElement):
    """Interact with <img> html tags."""

    tag = "img"


class Video(XPathElement):
    """Interact with <video> html tags."""

    tag = "video"


class Iframe(XPathElement):
    """Interact with <iframe> html tags."""

    tag = "iframe"


class Picture(XPathElement):
    """Interact with <picture> html tags."""

    tag = "picture"


class Source(XPathElement):
    """Interact with <source> html tags."""

    tag = "source"
