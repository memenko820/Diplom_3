import allure

import data
from locators.order_feed_page_locators import OrderFeedPageLocators
from pages.base_page import BasePage


class OrderFeedPage(BasePage):
    
    def wait_until_feed_loaded(self):
        self.wait_until(lambda driver: self._read_count(OrderFeedPageLocators.TOTAL_ORDERS_COUNTER) > 0)

    @allure.step('Открыть ленту заказов')
    def open_page(self):
        self.open_url(data.FEED_URL)
        self.wait_until_feed_loaded()

    def get_heading_text(self):
        return self.get_text(OrderFeedPageLocators.HEADING)

    def get_total_orders_count(self):
        return self._get_loaded_count(OrderFeedPageLocators.TOTAL_ORDERS_COUNTER)

    def get_today_orders_count(self):
        return self._get_loaded_count(OrderFeedPageLocators.TODAY_ORDERS_COUNTER)

    def is_total_orders_count_greater_than(self, value):
        return self.is_condition_met(lambda driver: self._read_count(OrderFeedPageLocators.TOTAL_ORDERS_COUNTER) > value)

    def is_today_orders_count_greater_than(self, value):
        return self.is_condition_met(lambda driver: self._read_count(OrderFeedPageLocators.TODAY_ORDERS_COUNTER) > value)

    def is_order_displayed(self, order_number):
        return self.is_element_visible(self.format_locator(OrderFeedPageLocators.ORDER_CARD, order_number=order_number))

    def is_order_in_progress(self, order_number):
        return self.is_element_visible(
            self.format_locator(OrderFeedPageLocators.IN_PROGRESS_ORDER, order_number=order_number))

    def _read_count(self, locator):
        text = self.driver.find_element(*locator).text
        return int(text) if text.isdigit() else 0

    def _get_loaded_count(self, locator):
        # Счётчик сначала пустой или нулевой, пока не придут данные с сервера
        self.wait_until(lambda driver: self._read_count(locator) > 0)
        return self._read_count(locator)

    @allure.step('Нажать на заказ в ленте')
    def click_first_order(self):
        self.click(OrderFeedPageLocators.FIRST_ORDER_CARD)

    def is_order_details_modal_displayed(self):
        return self.is_element_visible(OrderFeedPageLocators.ORDER_MODAL_CONTENT)