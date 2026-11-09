import allure

import data
from locators.forgot_password_page_locators import ForgotPasswordPageLocators
from pages.base_page import BasePage


class ForgotPasswordPage(BasePage):

    @allure.step('Открыть страницу восстановления пароля')
    def open_page(self):
        self.open_url(data.FORGOT_PASSWORD_URL)

    def get_heading_text(self):
        return self.get_text(ForgotPasswordPageLocators.HEADING)

    @allure.step('Ввести email')
    def set_email(self, email):
        self.type_text(ForgotPasswordPageLocators.EMAIL_INPUT, email)

    @allure.step('Нажать "Восстановить"')
    def click_restore_button(self):
        self.click(ForgotPasswordPageLocators.RESTORE_BUTTON)