"""
Module containing DuckDuckGoSearchPageClick
the page object for the DuckDuckGo search page
searching by click instead of RETURN
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class DuckDuckGoSearchPageClick:
    # URL
    URL = "https://duckduckgo.com/"

    # Locators
    SEARCH_INPUT = (By.ID, "searchbox_input")
    SEARCH_BUTTON = (By.CLASS_NAME, "searchbox_searchButton__F5Bwq")

    # Initializer
    def __init__(self, browser):
        self.browser = browser

    # Interaction methods
    def load(self):
        self.browser.get(self.URL)

    def search(self, phrase):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(phrase)
        search_click = self.browser.find_element(*self.SEARCH_BUTTON)
        search_click.click()
