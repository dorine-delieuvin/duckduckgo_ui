"""
Module containingshared fixtures
"""

import json
import pytest
import selenium.webdriver


@pytest.fixture
def config(scope="session"):
    # read file
    with open("config.json") as config_file:
        config = json.load(config_file)

    # assert values are acceptable
    assert config["browser"] in ["Firefox", "Chrome", "Headless Chrome"]
    assert isinstance(config["implicit_wait"], int)
    assert config["implicit_wait"] > 0

    # return config so it can be used
    return config


@pytest.fixture
def browser(config):
    # initialise Chromedriver instance
    if config["browser"] == "Firefox":
        b = selenium.webdriver.Firefox()
    elif config["browser"] == "Chrome":
        b = selenium.webdriver.Chrome()
    elif config["browser"] == "Headless Chrome":
        opts = selenium.webdriver.ChromeOptions()
        opts.add_argument("headless")
        b = selenium.webdriver.Chrome(options=opts)
    else:
        raise Exception(f"Browser '{config['browser']}' is not supported.")

    # make calls wait up to 10sec for element to appear
    b.implicitly_wait(config["implicit_wait"])

    # reurn Webdriver instance for the setup
    yield b

    # quit the Webdriver instance for the cleanup
    b.quit()
