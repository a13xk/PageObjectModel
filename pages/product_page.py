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

    def cart_item_title_matches_book_title(self):
        assert self.get_book_price() == self.get_cart_message_book_price(), "Tile mismatch"
    #

    def cart_item_price_matches_book_price(self):
        assert self.get_book_price() == self.get_cart_message_book_price(), "Price mismatch"
    #

    def should_not_be_success_message(self):
        assert self.is_element_absent(*ProductPageLocators.SUCCESS_MESSAGE_DIV1) and \
               self.is_element_absent(*ProductPageLocators.SUCCESS_MESSAGE_DIV2), "Success message is present, but must be absent"
    #

    def success_message_should_disappear(self):
        assert (self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE_DIV1) and
                self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE_DIV1)), "Success message must disappear, but is still on the page"
    #
#
