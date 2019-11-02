from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def click_add_to_cart(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()
    #

    def get_book_title(self):
        return self.browser.find_element(*ProductPageLocators.BOOK_TITLE_H1).text
    #

    def get_book_price(self):
        return self.browser.find_element(*ProductPageLocators.BOOK_PRICE_P).text
    #

    def get_cart_message_book_title(self):
        return self.browser.find_element(*ProductPageLocators.MESSAGE_BOOK_ADDED_TO_BASKET_TITLE).text
    #

    def get_cart_message_book_price(self):
        return self.browser.find_element(*ProductPageLocators.MESSAGE_BOOK_ADDED_TO_BASKET_PRICE).text
    #
#
