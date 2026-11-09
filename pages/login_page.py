import allure

import data
from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):

    @allure.step('Открыть страницу входа')
    def open_page(self):
        self.open_url(data.LOGIN_URL)

    def get_heading_text(self):
        return self.get_text(LoginPageLocators.HEADING)

    @allure.step('Нажать "Восстановить пароль"')
    def click_forgot_password_link(self):
        self.click(LoginPageLocators.FORGOT_PASSWORD_LINK)

    @allure.step('Войти под пользователем')
    def login(self, email, password):
        self.type_text(LoginPageLocators.EMAIL_INPUT, email)
        self.type_text(LoginPageLocators.PASSWORD_INPUT, password)
        self.click(LoginPageLocators.LOGIN_BUTTON)