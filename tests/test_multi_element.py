from pom_elements.multi_element import MultiElement


def test_multi_element(selenium_chrome):
    """Verify that the MultiElement class can be used."""
    selenium_chrome.get("https://xkcd.com/")
    xpath = MultiElement(
        webdriver=selenium_chrome, timeout=0.5, xpath='//a[@href="/archive"]'
    )
    assert xpath.is_visible()
