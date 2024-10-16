"""
Testing DuckDuckGo searches
using Pytest
"""

# to run tests sequencially
# pipenv run python -m pytest

# to run tests in parallel
# pipenv run python -m pytest -n 3

from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage
import pytest
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])


@pytest.mark.parametrize("phrase", ["panda", "python", "polar bear"])
def test_basic_duckduckgo_search(browser, phrase):
    search_page = DuckDuckGoSearchPage(browser)
    result_page = DuckDuckGoResultPage(browser)

    # GIVEN the DuckDuckGo home page is displayed
    search_page.load()

    # WHEN the user searches for "panda"
    search_page.search(phrase)

    # THEN the search result query is "panda"
    assert phrase == result_page.search_input_value()

    # AND the search result links pertain to "panda"
    titles = result_page.result_link_titles()
    matches = [t for t in titles if phrase.lower() in t.lower()]
    assert len(matches) > 0

    # AND the search result contains "panda"
    assert phrase in result_page.title()


print("testing some more stuff")
