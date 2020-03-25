from selenium import webdriver


def test_chrome():
    """Verify that the test runner can run Chrome locally."""
    driver = webdriver.Chrome()
    driver.get("http://www.yahoo.com/")
    driver.quit()


def test_firefox():
    """Verify that the test runner can run FireFox locally."""
    browser = webdriver.Firefox()
    browser.get("http://www.yahoo.com")
    browser.quit()


def test_safari():
    """Verify that the test runner can run Safari locally."""
    browser = webdriver.Safari()
    browser.get("http://www.yahoo.com")
    browser.quit()
