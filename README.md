# Selenium XPath

The Selenium Xpath library makes writing Selenium testing much easier by making the web
elements first class citizens in the testing heirarchy.

# Setup/Tools

## Things you'll need

- [Pyenv](https://github.com/pyenv/pyenv) or Python 3.8.2
  - Run `pip install pyenv`
  - Download Python 3.8.2 with `pyenv install 3.8.2`
  - The Python version should be set with the `.python-version` file at the root of the
    project.
- [Poetry](https://python-poetry.org/)
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

## Quickstart

1. Run `make build` to get setup.
   - This will install Poetry (a Python package management tool) and allow and setup the
     necessary dependencies for this project.s

## Testing

### Coverage Report

To run the coverage reporting tool run `make coverage`.

To view the coverage reporting run `make view-coverage-report`.
