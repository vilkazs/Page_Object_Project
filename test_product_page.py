from .pages.links import MainPageLinks
from .pages.links import ProductPageLinks
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from selenium.webdriver.common.by import By
import pytest
import time


@pytest.mark.parametrize('links', ProductPageLinks.PROMO_PAGES_LINKS)
def test_guest_can_add_product_to_basket(browser, links):
    page = ProductPage(browser, links)
    page.open()
    page.add_item_to_card_on_product_page()


@pytest.mark.login
class TestLogin():

    def test_guest_should_see_login_link_on_product_page(self, browser):
        page = ProductPage(browser, f"{MainPageLinks.MAIN_LINK}{ProductPageLinks.PRODUCT_LINK}", 0)
        page.open()
        page.should_be_login_link()

    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        page = ProductPage(browser, f"{MainPageLinks.MAIN_LINK}{ProductPageLinks.PRODUCT_LINK}")
        page.open()
        page.go_to_login_page()
    
    @pytest.mark.xfail(reason="Can't go to login page from product page because LOGIN_LINK_INVALID. It's negative test.")
    def test_guest_cant_go_to_login_page_from_product_page(self, browser):
        page = ProductPage(browser, f"{MainPageLinks.MAIN_LINK}{ProductPageLinks.PRODUCT_LINK}")
        page.open()
        page.not_go_to_login_page()


@pytest.mark.basket
class TestBasket():

    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        page = ProductPage(browser, ProductPageLinks.PROMO_PAGES_LINKS[0])
        page.open()
        page.go_to_basket_on_header()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.basket_is_empty_on_basket_page() 

    @pytest.mark.xfail(reason="Basket is empty. It's negative test.")
    def test_guest_can_see_product_in_basket_opened_from_product_page(self, browser):
        page = ProductPage(browser, ProductPageLinks.PROMO_PAGES_LINKS[0])
        page.open()
        page.go_to_basket_on_header()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.basket_is_not_empty_on_basket_page()

    @pytest.mark.xfail(reason="Can't go to basket page from product page because the button to go to basket is not presented on main page. It's negative test.")
    def test_guest_cant_go_to_login_page_from_product_page(self, browser):
        page = ProductPage(browser, ProductPageLinks.PROMO_PAGES_LINKS[0])
        page.open()
        page.should_not_be_button_view_basket_on_header()


@pytest.mark.negative
class TestNegative():

    @pytest.mark.xfail
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        page = ProductPage(browser, ProductPageLinks.PROMO_PAGES_LINKS[0], 0)
        page.open()                                 # Открываем страницу товара 
        page.add_item_to_card_on_product_page()     # Добавляем товар в корзину
        page.should_not_be_success_message()        # Проверка, что нет сообщения об успехе (is_not_element_present)

    def test_guest_cant_see_success_message(self, browser): 
        page = ProductPage(browser, ProductPageLinks.PROMO_PAGES_LINKS[0], 0)
        page.open()                                 # Открываем страницу товара
        page.should_not_be_success_message()        # Проверка, что нет сообщения об успехе (is_not_element_present)
    
    @pytest.mark.xfail
    def test_message_disappeared_after_adding_product_to_basket(self, browser): 
        page = ProductPage(browser, ProductPageLinks.PROMO_PAGES_LINKS[0], 0)
        page.open()                                 # Открываем страницу товара 
        page.add_item_to_card_on_product_page()     # Добавляем товар в корзину
        page.should_not_be_disappeared_message()    # Проверка, что нет сообщения об успехе (is_disappeared)


@pytest.mark.user_login
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.page = LoginPage(browser, MainPageLinks.LOG_LINK)
        self.page.open()                            # открыть страницу регистрации
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time())
        self.page.register_new_user(email, password)# зарегистрировать нового пользователя
        self.page.should_be_authorized_user()       # проверить, что пользователь залогинен
  
    
    def test_user_cant_see_success_message(self, browser): 
        page = ProductPage(browser, ProductPageLinks.PROMO_PAGES_LINKS[0])
        page.open()
        page.should_not_be_success_message()
    
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, ProductPageLinks.PROMO_PAGES_LINKS[0])
        page.open()
        page.add_item_to_card_on_product_page()
        