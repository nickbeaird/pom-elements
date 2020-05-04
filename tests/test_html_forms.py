from pom_elements.html import (
    Button,
    DataList,
    Fieldset,
    Form,
    Input,
    Label,
    Legend,
    Meter,
    OptGroup,
    Option,
    Select,
    TextArea,
)


def test_html_forms_element_Button():
    """Verify that Button Element returns the accurate xpath."""
    elem = Button()
    assert elem.xpath == "//button"


def test_html_forms_element_DataList():
    """Verify that DataList Element returns the accurate xpath."""
    elem = DataList()
    assert elem.xpath == "//datalist"


def test_html_forms_element_Fieldset():
    """Verify that Fieldset Element returns the accurate xpath."""
    elem = Fieldset()
    assert elem.xpath == "//fieldset"


def test_html_forms_element_Form():
    """Verify that Form Element returns the accurate xpath."""
    elem = Form()
    assert elem.xpath == "//form"


def test_html_forms_element_Input():
    """Verify that Input Element returns the accurate xpath."""
    elem = Input()
    assert elem.xpath == "//input"


def test_html_forms_element_Label():
    """Verify that Label Element returns the accurate xpath."""
    elem = Label()
    assert elem.xpath == "//label"


def test_html_forms_element_Legend():
    """Verify that Legend Element returns the accurate xpath."""
    elem = Legend()
    assert elem.xpath == "//legend"


def test_html_forms_element_Meter():
    """Verify that Meter Element returns the accurate xpath."""
    elem = Meter()
    assert elem.xpath == "//meter"


def test_html_forms_element_OptGroup():
    """Verify that OptGroup Element returns the accurate xpath."""
    elem = OptGroup()
    assert elem.xpath == "//optgroup"


def test_html_forms_element_Option():
    """Verify that Option Element returns the accurate xpath."""
    elem = Option()
    assert elem.xpath == "//option"


def test_html_forms_element_Select():
    """Verify that Select Element returns the accurate xpath."""
    elem = Select()
    assert elem.xpath == "//select"


def test_html_forms_element_TextArea():
    """Verify that TextArea Element returns the accurate xpath."""
    elem = TextArea()
    assert elem.xpath == "//textarea"
