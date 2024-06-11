from .pages.links import MainPageLinks
from .pages.login_page import LoginPage
from selenium.webdriver.common.by import By


def test_guest_can_go_to_login_page(browser):
    page = LoginPage(browser, MainPageLinks.MAIN_LINK) 
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

def test_guest_should_see_login_link(browser):
    page = LoginPage(browser, MainPageLinks.MAIN_LINK)
    page.open()
    page.should_be_login_link()
    