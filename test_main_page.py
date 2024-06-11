from .pages.links import MainPageLinks
from .pages.main_page import MainPage
from .pages.basket_page import BasketPage
from selenium.webdriver.common.by import By
import pytest


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = MainPage(browser, MainPageLinks.MAIN_LINK)
    page.open()
    page.go_to_basket_on_header()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.basket_is_empty_on_basket_page()


@pytest.mark.negative
class TestNegative():
    
    @pytest.mark.xfail(reason="Basket is empty. It's negative test.")
    def test_guest_can_see_product_in_basket_opened_from_main_page(self, browser):
        page = MainPage(browser, MainPageLinks.MAIN_LINK)
        page.open()
        page.go_to_basket_on_header()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.basket_is_not_empty_on_basket_page()

    @pytest.mark.xfail(reason="Can't go to basket page from main page because the button to go to basket is not presented on main page. It's negative test.")
    def test_guest_cant_go_to_basket_page_from_main_page(self, browser):
        page = MainPage(browser, MainPageLinks.MAIN_LINK)
        page.open()
        page.should_not_be_button_view_basket_on_header()
    