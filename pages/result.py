"""
Module containing DuckDuckGoResultPage
the page object for the DuckDuckGo result page
"""

from selenium.webdriver.common.by import By


class DuckDuckGoResultPage:

    # Locators
    RESULT_LINKS = (By.CSS_SELECTOR, "a.LQNqh2U1kzYxREs65IJu")
    RESULT_SNIPETS = (By.CSS_SELECTOR, "span.kY2IgmnCmOGjharHErah")
    SEARCH_INPUT = (By.ID, "search_form_input")

    # Initializer
    def __init__(self, browser):
        self.browser = browser

    # Interaction methods
    def result_link_titles(self):
        links = self.browser.find_elements(*self.RESULT_LINKS)
        titles = [link.text for link in links]
        return titles

    def result_snipets(self):
        results = self.browser.find_elements(*self.RESULT_SNIPETS)
        snipets = [snipet.text for snipet in results]
        return snipets

    def search_input_value(self):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        value = search_input.get_attribute("value")
        return value

    def title(self):
        return self.browser.title
