import math

from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from .locators import BasePageLocators


class BasePage:

    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(time_to_wait=timeout)
    #

    def is_element_present(self, how, what):
        """
        Check that element IS present on page
        :param how: Selection method
        :param what: Selector
        """
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True
    #

    def is_element_absent(self, how, what, timeout=4):
        """
        Within the given timeout, check that element is NOT present on page.
        If element is found, returns False.
        :param how: Selection method
        :param what: Selector
        :param timeout: Timeout
        """
        try:
            WebDriverWait(driver=self.browser,
                          timeout=timeout).until(method=EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False
    #

    def is_disappeared(self, how, what, timeout=4):
        """
        Within given timeout, check that element has disappeared from page.
        In element is still on the page, returns False
        :param how: Selection method
        :param what: Selector
        :param timeout: Timeout
        """
        try:
            WebDriverWait(driver=self.browser,
                          timeout=timeout,
                          poll_frequency=1,
                          ignored_exceptions=TimeoutException).until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True
    #

    def open(self):
        self.browser.get(self.url)
    #

    def go_to_login_page(self):
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()
    #

    def go_to_cart_page(self):
        cart_link = self.browser.find_element(*BasePageLocators.CART_LINK)
        cart_link.click()
    #

    def check_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"
    #

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
    #

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"
#
