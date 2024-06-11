from selenium.webdriver.common.by import By
    
class ProductPageLocators():
    BUTTON_ADD_TO_CARD      = (By.CSS_SELECTOR, "#add_to_basket_form > button")
    PRODUCT_NAME            = (By.CSS_SELECTOR, ".product_main > h1")
    PRODUCT_PRICE           = (By.CSS_SELECTOR, ".product_main .price_color")
    
    BASKET_MESSAGE          = (By.CSS_SELECTOR, ".alertinner > strong")
    BASKET_PRICE            = (By.CSS_SELECTOR, ".alertinner > p strong")

class BasketPageLocators():
    BASKET_MESSAGE_EMPTY    = (By.CSS_SELECTOR, "#content_inner")
    BASKET_ITEMS_TO_BUY_NOW = (By.CSS_SELECTOR, ".col-sm-6 .h3")

class BasePageLocators():
    LOGIN_LINK              = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID      = (By.CSS_SELECTOR, "#login_link_inc")
    BUTTON_VIEW_BASKET      = (By.CSS_SELECTOR, ".btn-group > .btn.btn-default")
    USER_ICON               = (By.CSS_SELECTOR, ".icon-user")

class LoginPageLocators():
    # login
    LOGIN_EMAIL             = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD          = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_BUTTON            = (By.CSS_SELECTOR, "#login_form > button")
    # registarition
    REG_EMAIL               = (By.CSS_SELECTOR, "#id_registration-email")
    REG_PASSWORD            = (By.CSS_SELECTOR, "#id_registration-password1")
    REG_PASSWORD_REPEAT     = (By.CSS_SELECTOR, "#id_registration-password2")
    REG_BUTTON              = (By.CSS_SELECTOR, "#register_form > button")
    