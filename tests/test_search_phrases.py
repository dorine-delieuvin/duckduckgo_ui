"""
Testing DuckDuckGo searches with different phrases
using Pytest
"""

# to run tests sequencially
# pipenv run python -m pytest

# to run tests in parallel
# pipenv run python -m pytest -n 3

from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage
import pytest


@pytest.mark.parametrize(
    "word, word_to_avoid",
    [("python", "snake"), ("python", "programming"), ("selenium", "testing")],
)
# Senario: search for "word" using the "-" advanced search operator
def test_duckduckgo_search_with_minus_operator(browser, word, word_to_avoid):
    search_page = DuckDuckGoSearchPage(browser)
    result_page = DuckDuckGoResultPage(browser)

    # GIVEN the DuckDuckGo home page is displayed
    search_page.load()

    # WHEN the user searches for "word -word_to_avoid"
    phrase = word + " -" + word_to_avoid
    search_page.search(phrase)

    # THEN the search result query is "word -word_to_avoid"
    assert phrase == result_page.search_input_value()

    # AND the search result links pertain to "word"
    titles = result_page.result_link_titles()
    matches = [t for t in titles if word.lower() in t.lower()]
    assert len(matches) > 0

    # AND the search result contains "word"
    assert phrase in result_page.title()

    # AND the search result titles do not contain "word_to_avoid"
    assert word_to_avoid not in result_page.result_link_titles()

    # AND the search result snipets do not contain "word_to_avoid"
    assert word_to_avoid not in result_page.result_snipets()

    # return Exception("Test not fully developed")
