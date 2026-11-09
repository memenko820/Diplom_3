import allure

import data
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage


@allure.feature('Основной функционал')
class TestMainFunctionality:

    @allure.title('Клик по "Конструктор" открывает конструктор')
    def test_click_constructor_link_opens_constructor(self, driver):
        login_page = LoginPage(driver)
        main_page = MainPage(driver)

        login_page.open_page()
        login_page.click_constructor_link()

        assert main_page.get_heading_text() == data.CONSTRUCTOR_HEADING

    @allure.title('Добавление ингредиента увеличивает его счётчик')
    def test_add_ingredient_increases_counter(self, driver, sauce):
        main_page = MainPage(driver)

        main_page.open_page()
        main_page.add_ingredient_to_constructor(sauce['_id'])

        assert main_page.is_ingredient_counter_equal(sauce['_id'], 1) is True

    @allure.title('Клик по "Лента Заказов" открывает ленту заказов')
    def test_click_order_feed_link_opens_order_feed(self, driver):
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)

        main_page.open_page()
        main_page.click_order_feed_link()

        assert order_feed_page.get_heading_text() == data.ORDER_FEED_HEADING

    @allure.title('Клик по ингредиенту открывает окно с деталями')
    def test_click_ingredient_opens_details_modal(self, driver, sauce):
        main_page = MainPage(driver)

        main_page.open_page()
        main_page.click_ingredient(sauce['_id'])

        assert main_page.get_ingredient_modal_heading_text() == data.INGREDIENT_MODAL_HEADING

    @allure.title('Окно с деталями ингредиента закрывается по клику на крестик')
    def test_click_close_button_closes_details_modal(self, driver, sauce):
        main_page = MainPage(driver)

        main_page.open_page()
        main_page.click_ingredient(sauce['_id'])
        main_page.close_modal()

        assert main_page.is_modal_closed() is True

    @allure.title('Залогиненный пользователь может оформить заказ')
    def test_logged_in_user_can_place_order(self, logged_in_driver, bun, sauce):
        main_page = MainPage(logged_in_driver)

        main_page.add_ingredient_to_constructor(bun['_id'])
        main_page.add_ingredient_to_constructor(sauce['_id'])
        main_page.click_place_order_button()

        assert main_page.is_order_number_displayed() is True