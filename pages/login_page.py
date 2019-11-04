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
        email_field = self.browser.find_element_by_css_selector(css_selector=LoginPageLocators.REGISTER_FORM_EMAIL[1])
        email_field.send_keys(email)

        password_field = self.browser.find_element_by_css_selector(css_selector=LoginPageLocators.REGISTER_FORM_PASSWORD[1])
        password_field.send_keys(password)

        confirm_password_field = self.browser.find_element_by_css_selector(css_selector=LoginPageLocators.REGISTER_FORM_PASSWORD_CONFIRM[1])
        confirm_password_field.send_keys(password)

        register_button = self.browser.find_element_by_css_selector(css_selector=LoginPageLocators.REGISTER_BUTTON[1])
        register_button.click()
        pass
    #

    @classmethod
    def generate_fake_email(cls):
        fake = Faker()
        email = fake.email()
        return email
    #

    @classmethod
    def generate_fake_password(cls):
        fake = Faker()
        password = fake.password(length=10, special_chars=True, digits=True, upper_case=True, lower_case=True)
        return password

#
