from pom_elements import XPathElement


class Button(XPathElement):
    """Interact with <button> html dom elements."""

    tag = "button"


class DataList(XPathElement):
    """Interact with <datalist> html dom elements."""

    tag = "datalist"


class Fieldset(XPathElement):
    """Interact with <fieldset> html dom elements."""

    tag = "fieldset"


class Form(XPathElement):
    """Interact with <form> html dom elements."""

    tag = "form"


class Input(XPathElement):
    """Interact with <input> html dom elements."""

    tag = "input"


class Label(XPathElement):
    """Interact with <label> html dom elements."""

    tag = "label"


class Legend(XPathElement):
    """Interact with <legend> html dom elements."""

    tag = "legend"


class Meter(XPathElement):
    """Interact with <meter> html dom elements."""

    tag = "meter"


class OptGroup(XPathElement):
    """Interact with <optgroup> html dom elements."""

    tag = "optgroup"


class Option(XPathElement):
    """Interact with <option> html dom elements."""

    tag = "option"


class Select(XPathElement):
    """Interact with <select> html dom elements."""

    tag = "select"


class TextArea(XPathElement):
    """Interact with <textarea> html dom elements."""

    tag = "textarea"
