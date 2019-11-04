from faker import Faker

from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()
    #

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, "Failed to open login URL"
    #

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM_USERNAME), "Login form username field not found"
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM_PASSWORD), "Login form password field not found"
    #

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM_EMAIL), "Register form email field not found"
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM_PASSWORD), "Register form password field not found"
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM_PASSWORD_CONFIRM), "Register form confirm password field not found"
    #

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_EMAIL)
        email_field.send_keys(email)

        password_field = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_PASSWORD)
        password_field.send_keys(password)

        confirm_password_field = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_PASSWORD_CONFIRM)
        confirm_password_field.send_keys(password)

        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()
    #
#
