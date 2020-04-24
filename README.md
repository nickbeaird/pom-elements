# POM-Elements

The POM-Elements project allows for organizing tests using the Page Object Pattern and
extending PageObjects with powerful PageElements as well. The Elements classes allows
test writers to interact with any page Locator type in the DOM and are designed as
ajax-friendly selectors. Additional features have been added to the xpath selctor
XPathElement PageObject Element class.

# Examples - Page Elements

```python
# Write tests by interacting with individual Page Elements using any locator.
element = MultiElement(
            css="#recordlist li:nth-child(4)",
            webdriver=selenium,
            timeout=5
          )
element.is_visible()
element.click()

# Or simplify what would be complex xpath paths with the the XPathElement.
xpath_element = XPathElement(
                  webdriver=selenium,
                  xpath='//a',
                  html_id='foo',
                  tag='bar',
                  timeout=3
                )
xpath_element.xpath   # '//a[@id="foo"][@tag="bar"]'
xpath_element.is_visible()
xpath_element.click()

```

# Examples - Page Elements

```python

# Organize your tests around a Page.
page = PageObject(
          webdriver=selenium,
          url='http://google.com'
       )

# Or a section of a page as an individual PageObject.
widget = PageObject(
            webdriver=selenium
         )


# Putting it all togher allows organizing entire pages with PageObjects and PageElements...
class PageHeader(PageObject):
    dropdown = MultiElement(css="div > a")

class PageFooter(PageObject):
    logo = XPath(xpath='//img')

class MyPage(PageObject):
    header = PageHeader()
    footer = PageFooter()

# Set the webdriver on the Parent PageObject instance...
mypage = MyPage(webdriver=selenium)
mypage.header.dropdown.is_visible()

# ...and access the webdriver on all instances of the PageObject or Element set on them.
mypage.footer.click()
```

# Design Choices

The project was designed with a few key thoughts in mind:

1. Allow test organization to mirror how your web page is organized (PageObjects).
1. Test writers can use individual Elements or add Elements to any PageObject heirarchy.
1. PageObjects can have any number of nested PageObjects without needing to manually
   hand off the webdriver to each PageObject (Data Descriptor Protocol).
1. Allow test writers to use any Selenium object locator that they prefer (MultiElement).
1. Improve the experience of debugging PageElement tests through the use of the Data
   Descriptor Protocol. Each Element is retrieved every time it is accessed. (see Debugging)

# Webdrivers

This project currently only supports a Python Selenium webdriver. The project has also
been tested with Pytest and Unittest class designs. Please feel free to add any additional
framework support. You may need the following to get started with this project.

- [ChromeDriver](https://chromedriver.chromium.org/)
  - Download [Chrome](https://www.google.com/chrome/)
  - Run `brew cask install chromedriver`
- [GeckoDriver](https://github.com/mozilla/geckodriver/releases)
  - Download [FireFox](https://www.mozilla.org/en-US/firefox/new/)
  - Download the GeckoDriver.
    - Find the release that matches your FireFox browser version.
    - If you are running this on a Mac on OSCatalina or newer, then follow the steps
      listed for [Mac notorization of ChromeDriver](https://firefox-source-docs.mozilla.org/testing/geckodriver/Notarization.html)
- [SafariDriver](https://developer.apple.com/documentation/webkit/testing_with_webdriver_in_safari)
  - Follow the instructions listed in the link above.
