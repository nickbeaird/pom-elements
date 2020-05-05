![Run Checks](https://github.com/nickbeaird/pom-elements/workflows/Run%20Checks/badge.svg?branch=master)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![CodeFactor](https://www.codefactor.io/repository/github/nickbeaird/pom-elements/badge?s=32178acb85e5cbeb67ab7378f6796de066ec16dd)](https://www.codefactor.io/repository/github/nickbeaird/pom-elements)

## pom-elements

The Python package `pom-elements` for a Page Object Model that extends to Page Elements.

[Github](https://github.com/nickbeaird/pom-elements/)

[Documentation](https://nickbeaird.github.io/pom-elements/)

## Installation

    $ pip install pom-elements

## Usage

Organize your ui-tests in Classes that represent you page designs. Also organize all of the selectors for your tests with Page Elements.

## Features

- Organize your tests to reflect how your web page is desinged (Page Objects).
- Augment your current tests by using through the organization of Pages, PageObjects, or individual Elements.
- Allows test writers to bring their favorite locator of choice (MultiElement).
- Use any number of nested PageObjects without needing to manually hand off a webdriver to each instance.
- Improve the experience of debugging through geting the Element on every call (Descriptor Protocol).

## Webdrivers

This project currently supports the Python Selenium webdriver. The project has been tested with Pytest and Unittest class designs. Please feel free to add any additional framework support. You may need the following to get started with this project.

- [ChromeDriver](https://chromedriver.chromium.org/)
- [GeckoDriver](https://github.com/mozilla/geckodriver/releases)
- [Selenium-Grid](https://www.selenium.dev/documentation/en/grid/)
