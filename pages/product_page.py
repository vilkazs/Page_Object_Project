from .base_page import BasePage
from .locators import ProductPageLocators
import time


class ProductPage(BasePage):
    def add_item_to_card_on_product_page(self):
        self.should_be_promo_url()
        self.should_be_button_add_to_card()
        self.should_be_item_added_to_card()
        # message
        self.should_be_name_of_item()
        self.should_be_price_of_item()

    def should_be_promo_url(self):
        assert "?promo=" in self.browser.current_url, f"the url does not contain '?promo='"

    def should_be_button_add_to_card(self):
        assert self.is_element_present(*ProductPageLocators.BUTTON_ADD_TO_CARD), f"Add to card button is not presented on the product page"

    def should_be_item_added_to_card(self):
        button_add_to_card = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_CARD)
        button_add_to_card.click()
        self.solve_quiz_and_get_code()
        
    def should_be_name_of_item(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        basket_message = self.browser.find_element(*ProductPageLocators.BASKET_MESSAGE).text
        #print("product_name =", product_name)
        #print("basket_message =", basket_message)
        assert product_name == basket_message, f"Product name does not match message."
        
    def should_be_price_of_item(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
        #print("product_price =", product_price)
        #print("basket_price =", basket_price)
        assert product_price == basket_price, f"The cart price does not match the product price."
    
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.BASKET_MESSAGE), \
           "Success message is presented, but should not be"
           
    def should_not_be_disappeared_message(self):
        assert self.is_disappeared(*ProductPageLocators.BASKET_MESSAGE), \
       "Success message is not disappeared, but should be"
    