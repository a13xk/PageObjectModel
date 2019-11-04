import pytest

from .pages.cart_page import CartPage
from .pages.login_page import LoginPage
from .pages.main_page import MainPage


@pytest.mark.login_guest
class TestLoginFromMainPage:

    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser=browser, url=browser.current_url)

        # Assertions
        login_page.should_be_login_page()
    #

    def test_login_link_available_for_guest(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()

        # Assertions
        page.check_login_link()
    #
#


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_cart_page()
    cart_page = CartPage(browser=browser, url=browser.current_url)

    # Assertions
    cart_page.should_be_cart_page()
    cart_page.should_not_be_any_items_in_cart()
    cart_page.should_be_text_of_no_items_in_cart()
#
