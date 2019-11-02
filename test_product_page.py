import pytest
import time

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


@pytest.mark.parametrize(argnames='link', argvalues=links())
def test_guest_can_add_product_to_cart(browser, link):
    # link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    # link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser=browser, url=link)
    page.open()
    page.click_add_to_cart()
    page.solve_quiz_and_get_code()
    # time.sleep(100_000_000)
    assert page.get_book_title() == page.get_cart_message_book_title(), "Tile mismatch"
    assert page.get_book_price() == page.get_cart_message_book_price(), "Price mismatch"
#


@pytest.mark.xfail(reason="This check is inverted for test purposes")
def test_guest_cant_see_success_message_after_adding_product_to_cart(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser=browser, url=link)
    page.open()
    page.click_add_to_cart()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()
#


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser=browser, url=link)
    page.open()
    page.should_not_be_success_message()
#


@pytest.mark.xfail(reason="Success message stays on page for test purposes")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser=browser, url=link)
    page.open()
    page.click_add_to_cart()
    page.solve_quiz_and_get_code()
    page.success_message_should_disappear()
#
