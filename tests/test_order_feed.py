import allure

import helpers
from pages.order_feed_page import OrderFeedPage
from pages.order_history_page import OrderHistoryPage


@allure.feature('Лента заказов')
class TestOrderFeed:

    @allure.title('Клик по заказу в ленте открывает окно с деталями заказа')
    def test_click_order_opens_order_details_modal(self, driver):
        order_feed_page = OrderFeedPage(driver)

        order_feed_page.open_page()
        order_feed_page.click_first_order()

        assert order_feed_page.is_order_details_modal_displayed() is True

    @allure.title('Заказ из истории заказов отображается в ленте заказов')
    def test_order_from_history_is_displayed_in_order_feed(self, logged_in_driver, create_order):
        history_page = OrderHistoryPage(logged_in_driver)
        order_feed_page = OrderFeedPage(logged_in_driver)

        create_order()
        history_page.click_personal_account_link()
        history_page.click_order_history_link()
        order_number = history_page.get_first_order_number()
        history_page.click_order_feed_link()

        assert order_feed_page.is_order_displayed(order_number) is True

    @allure.title('При создании заказа счётчик "Выполнено за все время" увеличивается')
    def test_create_order_increases_total_orders_counter(self, driver, create_order):
        order_feed_page = OrderFeedPage(driver)

        order_feed_page.open_page()
        total_before = order_feed_page.get_total_orders_count()
        create_order()

        assert order_feed_page.is_total_orders_count_greater_than(total_before) is True

    @allure.title('При создании заказа счётчик "Выполнено за сегодня" увеличивается')
    def test_create_order_increases_today_orders_counter(self, driver, create_order):
        order_feed_page = OrderFeedPage(driver)

        order_feed_page.open_page()
        today_before = order_feed_page.get_today_orders_count()
        create_order()

        assert order_feed_page.is_today_orders_count_greater_than(today_before) is True

    @allure.title('Номер нового заказа появляется в разделе "В работе"')
    def test_create_order_shows_order_number_in_progress(self, driver, create_order):
        order_feed_page = OrderFeedPage(driver)

        order_feed_page.open_page()
        order_number = create_order()

        assert order_feed_page.is_order_in_progress(helpers.format_order_number(order_number)) is True