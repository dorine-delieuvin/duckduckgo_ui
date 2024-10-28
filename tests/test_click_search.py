"""
Testing DuckDuckGo search by clicking the search button
instead of RETURN
using Pytest
"""

# to run tests sequencially
# pipenv run python -m pytest

# to run tests in parallel
# pipenv run python -m pytest -n 3

from pages.result import DuckDuckGoResultPage
from pages.search_click import DuckDuckGoSearchPageClick
import pytest
import re


## Tests Setup/Cleanup
@pytest.fixture(scope="function", autouse=True)
def before_each_after_each(browser):
    search_page = DuckDuckGoSearchPageClick(browser)

    # GIVEN the DuckDuckGo home page is displayed
    yield search_page.load()


@pytest.mark.parametrize("phrase", ["panda", "python", "polar bear"])
def test_basic_duckduckgo_search(browser, phrase):
    search_page = DuckDuckGoSearchPageClick(browser)
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
