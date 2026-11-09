import allure
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import data
from locators.base_page_locators import BasePageLocators
from locators.header_locators import HeaderLocators


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        self.driver.get(url)

    def wait_for_url(self, url):
        WebDriverWait(self.driver, data.WAIT_TIMEOUT).until(EC.url_to_be(url))

    def wait_until(self, condition):
        return WebDriverWait(self.driver, data.WAIT_TIMEOUT, ignored_exceptions=[StaleElementReferenceException]).until(
            condition)

    def is_condition_met(self, condition):
        try:
            self.wait_until(condition)
        except TimeoutException:
            return False
        return True

    def wait_for_visible(self, locator):
        return self.wait_until(EC.visibility_of_element_located(locator))

    def wait_for_overlay_to_disappear(self):
        self.wait_until(lambda driver: not any(
            overlay.is_displayed() for overlay in driver.find_elements(*BasePageLocators.MODAL_OVERLAY)))

    def click_element(self, locator):
        self.wait_until(EC.element_to_be_clickable(locator)).click()

    def click(self, locator):
        self.wait_for_overlay_to_disappear()
        self.click_element(locator)

    def type_text(self, locator, text):
        self.wait_for_visible(locator).send_keys(text)

    def get_text(self, locator):
        return self.wait_for_visible(locator).text

    def format_locator(self, locator, **kwargs):
        by, value = locator
        return by, value.format(**kwargs)

    def is_element_visible(self, locator):
        return self.is_condition_met(EC.visibility_of_element_located(locator))

    def is_text_equal(self, locator, text):
        return self.is_condition_met(lambda driver: driver.find_element(*locator).text == text)

    @allure.step('Закрыть всплывающее окно крестиком')
    def close_modal(self):
        self.click_element(BasePageLocators.MODAL_CLOSE_BUTTON)

    def is_modal_closed(self):
        return self.is_condition_met(EC.invisibility_of_element_located(BasePageLocators.OPENED_MODAL))

    @allure.step('Нажать "Конструктор" в шапке')
    def click_constructor_link(self):
        self.click(HeaderLocators.CONSTRUCTOR_LINK)

    @allure.step('Нажать "Лента Заказов" в шапке')
    def click_order_feed_link(self):
        self.click(HeaderLocators.ORDER_FEED_LINK)

    @allure.step('Нажать "Личный Кабинет" в шапке')
    def click_personal_account_link(self):
        self.click(HeaderLocators.PERSONAL_ACCOUNT_LINK)