from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
#


class LoginPageLocators:
    LOGIN_FORM_USERNAME = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_FORM_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    REGISTER_FORM_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_FORM_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_FORM_PASSWORD_CONFIRM = (By.CSS_SELECTOR, "#id_registration-password2")
#


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    BOOK_TITLE_H1 = (By.CSS_SELECTOR, ".product_main > h1")
    BOOK_PRICE_P = (By.CSS_SELECTOR, ".product_main > p.price_color")
    MESSAGE_BOOK_ADDED_TO_BASKET_TITLE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    MESSAGE_BOOK_ADDED_TO_BASKET_PRICE = (By.CSS_SELECTOR, "#messages > div:nth-child(3) > div > p > strong")
    SUCCESS_MESSAGE_DIV1 = (By.CSS_SELECTOR, "#messages > div:nth-child(1)")
    SUCCESS_MESSAGE_DIV2 = (By.CSS_SELECTOR, "#messages > div:nth-child(2)")
#
