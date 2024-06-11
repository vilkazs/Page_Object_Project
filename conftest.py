import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
                     
    parser.addoption('--language', action='store', default='en',
                     help="Choose language: '--language=en' or '--language=ru' or 'Other language'")

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
     
    browser = None
    if browser_name == "chrome":
        print(f"\nstart {browser_name} browser for test..")
        options = webdriver.ChromeOptions()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)        
    elif browser_name == "firefox":
        print(f"\nstart {browser_name} browser for test..")
        options=Options()
        firefox_profile = FirefoxProfile()
        firefox_profile.set_preference("intl.accept_languages", user_language)
        options.profile = firefox_profile
        browser = webdriver.Firefox(options=options)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    
    yield browser
    print("\nquit browser..")
    browser.quit()
