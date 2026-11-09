import allure

from locators.reset_password_page_locators import ResetPasswordPageLocators
from pages.base_page import BasePage


class ResetPasswordPage(BasePage):

    def get_save_button_text(self):
        return self.get_text(ResetPasswordPageLocators.SAVE_BUTTON)

    @allure.step('Нажать на иконку показать/скрыть пароль')
    def click_show_password_icon(self):
        self.click(ResetPasswordPageLocators.SHOW_PASSWORD_ICON)

    def is_password_field_highlighted(self):
        return self.is_element_visible(ResetPasswordPageLocators.PASSWORD_FIELD_ACTIVE)