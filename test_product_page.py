import time

import pytest

from .pages.base_page import BasePage
from .pages.cart_page import CartPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage


def links():
    return ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
            "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
            "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
            "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
            "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
            "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
            "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
            pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),     # Bugged link
            "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
            "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"]
#


class TestGuestAddToCartFromProductPage:

    @pytest.mark.need_review
    @pytest.mark.parametrize(argnames='link', argvalues=links())
    def test_guest_can_add_product_to_cart(self, browser, link):
        page = ProductPage(browser=browser, url=link)
        page.open()
        page.click_add_to_cart()
        page.solve_quiz_and_get_code()

        # Assertions
        page.cart_item_title_matches_book_title()
        page.cart_item_price_matches_book_price()
    #

    @pytest.mark.xfail(reason="This check is inverted for test purposes")
    def test_guest_cant_see_success_message_after_adding_product_to_cart(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        page = ProductPage(browser=browser, url=link)
        page.open()
        page.click_add_to_cart()
        page.solve_quiz_and_get_code()

        # Assertions
        page.should_not_be_success_message()
    #

    def test_guest_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        page = ProductPage(browser=browser, url=link)
        page.open()

        # Assertions
        page.should_not_be_success_message()
    #

    @pytest.mark.xfail(reason="Success message stays on page for test purposes")
    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        page = ProductPage(browser=browser, url=link)
        page.open()
        page.click_add_to_cart()
        page.solve_quiz_and_get_code()

        # Assertions
        page.success_message_should_disappear()
    #

    def test_guest_should_see_login_link_on_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()

        # Assertions
        page.check_login_link()
    #

    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser=browser, url=browser.current_url)

        # Assertions
        login_page.should_be_login_page()
    #

    @pytest.mark.need_review
    def test_guest_cant_see_product_in_cart_opened_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_cart_page()
        cart_page = CartPage(browser=browser, url=browser.current_url)

        # Assertions
        cart_page.should_be_cart_page()
        cart_page.should_not_be_any_items_in_cart()
        cart_page.should_be_text_of_no_items_in_cart()
    #
#


class TestUserAddToCartFromProductPage:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = BasePage(browser=browser, url=link)
        page.open()
        page.go_to_login_page()

        login_page = LoginPage(browser=browser, url=browser.current_url)
        login_page.should_be_login_page()

        fake_email = LoginPage.generate_fake_email()
        fake_password = LoginPage.generate_fake_password()
        time.sleep(1)
        login_page.register_new_user(email=fake_email,
                                     password=fake_password)

        # Assertions
        page.should_be_authorized_user()
    #

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        page = ProductPage(browser=browser, url=link)
        page.open()

        # Assertions
        page.should_not_be_success_message()
    #

    @pytest.mark.need_review
    def test_user_can_add_product_to_cart(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
        page = ProductPage(browser=browser, url=link)
        page.open()
        page.click_add_to_cart()
        page.solve_quiz_and_get_code()

        # Assertions
        page.cart_item_title_matches_book_title()
        page.cart_item_price_matches_book_price()
    #
#
