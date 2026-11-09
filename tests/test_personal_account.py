import allure

import data
from pages.profile_page import ProfilePage
from pages.login_page import LoginPage


@allure.feature('Личный кабинет')
class TestPersonalAccount:

    @allure.title('Клик по "Личный Кабинет" открывает профиль')
    def test_click_personal_account_link_opens_profile(self, logged_in_driver):
        profile_page = ProfilePage(logged_in_driver)

        profile_page.click_personal_account_link()

        assert profile_page.get_active_profile_link_text() == data.PROFILE_MENU_ITEM_TEXT

    @allure.title('Клик по "История заказов" открывает историю заказов')
    def test_click_order_history_link_opens_order_history(self, logged_in_driver):
        profile_page = ProfilePage(logged_in_driver)

        profile_page.click_personal_account_link()
        profile_page.click_order_history_link()

        assert profile_page.get_active_order_history_link_text() == data.ORDER_HISTORY_MENU_ITEM_TEXT

    @allure.title('Клик по "Выход" выводит из аккаунта на страницу входа')
    def test_click_logout_button_opens_login_page(self, logged_in_driver):
        profile_page = ProfilePage(logged_in_driver)
        login_page = LoginPage(logged_in_driver)

        profile_page.click_personal_account_link()
        profile_page.click_logout_button()

        assert login_page.get_heading_text() == data.LOGIN_HEADING