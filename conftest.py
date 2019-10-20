import pytest
from selenium.webdriver.chrome.options import Options
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default="en",
                     help="Select browser language: ru, en, es, fr, etc...")
    parser.addoption('--sleep_time', action='store', default=30,
                     help="Value for time.sleep() command in seconds")


@pytest.fixture(scope="function")
def sleep_time(request):
    return int(request.config.getoption("sleep_time"))


@pytest.fixture(scope="function")
def language(request):
    return request.config.getoption("language")


@pytest.fixture(scope="function")
def browser(request):

    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")

    if browser_name == "chrome":
        print(f"\nStart Chrome browser for test with language '{user_language}'")
        options = Options()
        options.add_experimental_option(name='prefs', value={'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print(f"\nStart Firefox browser for test with language '{user_language}'")
        fp = webdriver.FirefoxProfile()
        fp.set_preference(key="intl.accept_languages", value=user_language)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be 'chrome' or 'firefox'")

    yield browser

    print("\nquit browser..")
    browser.quit()
#
