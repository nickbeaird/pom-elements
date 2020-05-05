[GITHUB](https://github.com/nickbeaird/pom-elements/)

## Examples - Elements

Write tests using any `Selenium Locator` (i.e. css, id, xpath, name, etc.) of your choosing.

    >>> element = MultiElement(
    ...     css="#recordlist li:nth-child(4)",
    ...     webdriver=selenium,
    ...     timeout=5)
    ...
    >>> element.is_visible()
    True
    >>> element.click()

Or simplify complex xpath arguments with XPathElement.

    >>> xpath_element = XPathElement(
    ...                     webdriver=selenium,
    ...                     xpath='//a',
    ...                     foo='bar',
    ...                     baz='spam',
    ...                     timeout=3
    ...                 )
    >>> xpath_element.xpath
    '//a[@foo="bar"][@baz="spam"]'
    >>> xpath_element.is_invisible()
    False
    >>> xpath_element.can_be_clicked()
    True

## Examples - Page and PageObject

Organize your tests around a Page.

    >>> class GoogleHomePage(Page):
    ...     search_bar = XPathElemnent(xpath='//input', name="search")
    ...
    >>> google = GoogleHomePage(
    ...              webdriver=selenium,
    ...              url='http://google.com'
    ...           )
    >>> google.go()
    >>> google.current_url
    'https://www.google.com'
    >>> google.search_bar.send_keys('pom-elements is cool!')

Or a section of a page as an individual PageObject.

    >>> class Header(PageObject):
    ...     dropdown = XPathElement(xpath'//button', html_class="btn btn-secondary dropdown-toggle")
    ...
    >>> header = Header(webriver=webdriver)
    >>> header.dropdown.click()

Putting it all togher allows organizing entire pages with PageObjects and PageElements...

    >>> class PageHeader(PageObject):
    ...     dropdown = MultiElement(css="div > a")
    ...
    >>> class PageFooter(PageObject):
    ...     logo = XPath(xpath='//img[dat-attrib="best_image"]')
    ...
    >>> class MyPage(PageObject):
    ...     header = PageHeader()
    ...     footer = PageFooter()

...Set the webdriver on the Parent PageObject instance...

    >>> mypage = MyPage(webdriver=selenium)
    ...
    >>> mypage.header.dropdown.is_visible()
    True

...and access the webdriver on all instances of the PageObject or Element set on them.

    >>> mypage.footer.click()

## Example - HTML Elements

The `pom_elements.html` module is both a way to interact with all html dom elements, as
well a proof of concept for how one could organize classes for their own projects. Not
every html element has a direct html Element class, but common selectors do have classes
available in this library.

A common use case is to select attributes that live in a specific html div.

    >>> from pom_elements.html import Div
    >>> elem = Div(html_id="bar", text="Text that resides in a <div> element.")
    >>> elem.xath
    '//div[id="bar"][contains(text(), "Text that resides in a <div> element.")]'
    >>> elem.is_visible()
    True

## Features

- Organize your tests to reflect how your web page is desinged (Page Objects).
- Augment your current tests by using through the organization of Pages, PageObjects, or individual Elements.
- Allows test writers to bring their favorite locator of choice (MultiElement).
- Use any number of nested PageObjects without needing to manually hand off a webdriver to each instance.
- Improve the experience of debugging through geting the Element on every call (Descriptor Protocol).
