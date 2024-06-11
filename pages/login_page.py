from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()
    
    
    def should_be_login_url(self):
        assert "login" in self.browser.current_url, f"the url does not contain 'login'"

    def should_be_login_form(self):
        # проверка, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL), f"Login email is not presented on the login form"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD), f"Login password is not presented on the login form"
        assert self.is_element_present(*LoginPageLocators.LOGIN_BUTTON), f"Login button is not presented on the login form"

    def should_be_register_form(self):
        # проверка, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REG_EMAIL), f"Registration email is not presented on the register form"
        assert self.is_element_present(*LoginPageLocators.REG_PASSWORD), f"Registration password is not presented on the register form"
        assert self.is_element_present(*LoginPageLocators.REG_PASSWORD_REPEAT), f"Registration repeat password is not presented on the register form"
        assert self.is_element_present(*LoginPageLocators.REG_BUTTON), f"Registration button is not presented on the register form"
    
    def register_new_user(self, email, password):
        element_email = self.browser.find_element(*LoginPageLocators.REG_EMAIL)
        element_email.send_keys(email)

        element_password = self.browser.find_element(*LoginPageLocators.REG_PASSWORD)
        element_password.send_keys(password)

        element_password_repeat = self.browser.find_element(*LoginPageLocators.REG_PASSWORD_REPEAT)
        element_password_repeat.send_keys(password)

        button_reg = self.browser.find_element(*LoginPageLocators.REG_BUTTON)
        button_reg.click()
    