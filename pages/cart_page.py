from .base_page import BasePage
from .locators import CartPageLocators


class CartPage(BasePage):

    def should_be_cart_page(self):
        self.should_be_cart_url()
        # self.should_be_login_form()
        # self.should_be_register_form()
    #

    def should_be_cart_url(self):
        # реализуйте проверку на корректный url адрес
        assert "basket" in self.browser.current_url, "Failed to open login URL"
    #

    def should_not_be_any_items_in_cart(self):
        assert self.is_element_absent(*CartPageLocators.ITEMS_IN_CART_FORM), "Cart has items"
    #

    def should_be_text_of_no_items_in_cart(self):
        assert self.is_element_present(*CartPageLocators.NO_ITEMS_IN_CART_TEXT), "Message of cart has items"
    #
#
