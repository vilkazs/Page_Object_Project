from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def basket_is_empty_on_basket_page(self):
        self.should_be_basket_is_empty()
        self.should_be_text_that_the_basket_is_empty()

    def basket_is_not_empty_on_basket_page(self):
        self.should_be_basket_is_not_empty()
        self.should_be_text_that_the_basket_is_not_empty()
    
    def should_be_basket_is_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS_TO_BUY_NOW), f"Element 'Items to buy now' is presented on the basket page. Basket is not empty."

    def should_be_basket_is_not_empty(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_ITEMS_TO_BUY_NOW), f"Element 'Items to buy now' is presented on the basket page. Basket is empty."
    
    def should_be_text_that_the_basket_is_empty(self):
        basket_empty_message = self.browser.find_element(*BasketPageLocators.BASKET_MESSAGE_EMPTY).text
        assert "Your basket is empty." in basket_empty_message, f"The text is not about the basket being empty."
        
    def should_be_text_that_the_basket_is_not_empty(self):
        basket_not_empty_message = self.browser.find_element(*BasketPageLocators.BASKET_MESSAGE_EMPTY).text
        assert "Your basket is empty." in basket_not_empty_message, f"The text is about the basket being empty."
  