"""
Command-line tool for generating twitter images, given a gpt2-simple checkpoint.
"""

__version__ = "0.1.0"

from datetime import datetime

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located


def wait_for_element(css_selector: str) -> WebElement:
    """Wait for the provided CSS selector to appear."""
    return WebDriverWait(driver, 10).until(
        visibility_of_element_located((By.CSS_SELECTOR, css_selector))
    )


def edit_content(parent: str, content: str) -> None:
    """Replace the textContent of the provided span element."""
    element: WebElement = tweet_base.find_element_by_css_selector(
        f"{parent} > span[class='{span_selector}']"
    )
    driver.execute_script("arguments[0].textContent = arguments[1]", element, content)


options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
driver = webdriver.Chrome(chrome_options=options)

driver.get("https://twitter.com/benjomit/status/1330979032888958976")
tweet_base = wait_for_element(".css-1dbjc4n.r-j7yic.r-qklmqi.r-1adg3ll.r-1ny4l3l")
span_selector = "css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0"

edit_content(parent="a[target='_blank']", content="Twitter for GPT-2")


def make_tweet(message: str) -> bytes:
    """
    Make a tweet, given the provided text content.

    Take a screenshot of the tweet's element and return the bytes.
    """
    edit_content(parent="div[dir='auto'][lang='en']", content=message)
    edit_content(
        parent="a[role='link']",
        content=datetime.now().strftime("%-H:%M %p · %b %-d, %Y"),
    )
    return tweet_base.screenshot_as_png
