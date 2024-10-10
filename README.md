Practising UI testing on the DuckDuckGo search engine using Python.

Status of the Project: [Here]() (LINK TO BE ADDED)

Link to [DuckDuckGo Home Page](https://duckduckgo.com/)

See below how to set up the project to be able to run it successfully.

# Notes

This project is based on the project build along the _Introduction to Selenium WebDriver with Python_ course
taught by [Andrew "Pandy" Knight](https://twitter.com/AutomationPanda) on [Test Automation University](https://testautomationu.applitools.com/).
This project aims to create test cases to test other features of DuckDuckGo, to practice UI testing using Selenium WebDriver.

# Project Goals

The guided course covered one very basic search test, but DuckDuckGo has many more features.
This practice project aims to create automated scripts to test some of those features:

- search for different phrases

- search by clicking the button instead of typing RETURN

- click a search result

- expand "More Results" at the bottom of the result page

- verify auto-complete suggestions pertain to the search text

- search by selecting an auto-complete suggestion

- search a new phrase from the results page

- do an image search

- do a video search

- do a news search

- change settings

- change region

These tests will require new page objects, locators, and interaction methods.

# Setup Instructions

The following set-up instructions are adapted from the ones used for the course,
which can be found on the course [GitHub repository](https://github.com/AutomationPanda/tau-intro-selenium-py).

## Python Setup

All OS supported: Windows, macOS, Linux, etc.

This course requires Python 3.8 or higher. (Please update the "Pipfile" with the version of Python you are using.)
Latest Python version: [Python.org](https://www.python.org/downloads/).

This course also requires [pipenv](https://docs.pipenv.org/).
To install pipenv, run `pip install pipenv` from the command line.

You should also have a Python editor/IDE of your choice.
[PyCharm](https://www.jetbrains.com/pycharm/)
or [Visual Studio Code](https://code.visualstudio.com/docs/languages/python) for example.

You will also need [Git](https://git-scm.com/) to copy this project code.

## WebDriver Setup

For Web UI testing, you will need to install the latest versions of
[Google Chrome](https://www.google.com/chrome/)
and [Mozilla Firefox](https://www.mozilla.org/en-US/firefox/).
You can use other browsers with Selenium WebDriver, but the course will use Chrome and Firefox.

You will also need to install the latest versions of the WebDriver executables for these browsers:
[ChromeDriver](https://developer.chrome.com/docs/chromedriver/downloads) for Chrome
and [geckodriver](https://github.com/mozilla/geckodriver/releases) for Firefox.
Each test case will launch the WebDriver executable for its target browser.
The WebDriver executable will act as a proxy between the test automation and the browser instance.
Please use the latest versions of both the browsers and the WebDriver executables.
Older versions might be incompatible with each other.

ChromeDriver and geckodriver must be installed on the
[system path](<https://en.wikipedia.org/wiki/PATH_(variable)>).

### WebDriver Setup for Windows

To install ChromeDriver and geckodriver on Windows:

1. Create a folder named `C:\Selenium`.
2. Move the executables into this folder.
3. Add this folder to the _Path_ environment variable. (See [How to Add to Windows PATH Environment Variable](https://helpdeskgeek.com/windows-10/add-windows-path-environment-variable/).)

### WebDriver Setup for \*NIX

To install ChromeDriver and geckodriver on Linux, macOS, and other UNIX variants,
simply move them to the `/usr/local/bin/` directory:

```bash
$ mv /path/to/ChromeDriver /usr/local/bin
$ mv /path/to/geckodriver /usr/local/bin
```

This directory should already be included in the system path.
For troubleshooting, see:

- [Setting the path on macOS](https://www.cyberciti.biz/faq/appleosx-bash-unix-change-set-path-environment-variable/)
- [Setting the path on Linux](https://stackoverflow.com/questions/14637979/how-to-permanently-set-path-on-linux-unix)

### Test WebDriver Setup

To verify correct setup on any operating system, simply try to run them from the terminal:

```bash
$ ChromeDriver
$ geckodriver
```

You may or may not see any output.
Just verify that you can run them without errors.
Use Ctrl-C to kill them.

## Project Setup

1. Clone this repository.
2. Run `cd duckduckgo_ui` to enter the project.
3. Run `pipenv install` to install the dependencies.
4. Run `pipenv run python -m pytest` to verify that the framework can run tests.
5. Create a branch for your code changes. (See _Repository Branching_ below.)

### Project Setup Troubleshooting

A few people attempting to set up this project
encountered the following error when executing `pipenv run python -m pytest`:

```
ModuleNotFoundError: No module named 'atomicwrites'
```

I'm not exactly sure why `pipenv install` does not include `atomicwrites`.
So far, I have seen it happen only on Windows.
To resolve the error, please attempt the following:

- Upgrade Python to the latest versions. The following worked for me on Windows:
  - Python 3.8.3 (`python --version`)
  - pip 20.1 (`pip --version`)
  - pipenv 2018.11.26 (`pipenv --version`)
- Run `pipenv update` from within the project directory.

If upgrades don't work, try forcing package installation:

- Run `pipenv install pytest` from within the project directory.
- Run `pipenv install atomicwrites` from within the project directory.

If these steps don't work in your project, then try to run without pipenv:

- Install Python packages directly using `pip`.
- Run tests directly using `python -m pytest`.
