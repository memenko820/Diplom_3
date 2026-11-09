import allure

import data
from pages.forgot_password_page import ForgotPasswordPage
from pages.login_page import LoginPage
from pages.reset_password_page import ResetPasswordPage


@allure.feature('Восстановление пароля')
class TestPasswordRecovery:

    @allure.title('Ссылка "Восстановить пароль" открывает страницу восстановления')
    def test_click_forgot_password_link_opens_recovery_page(self, driver):
        login_page = LoginPage(driver)
        forgot_password_page = ForgotPasswordPage(driver)

        login_page.open_page()
        login_page.click_forgot_password_link()

        assert forgot_password_page.get_heading_text() == data.FORGOT_PASSWORD_HEADING

    @allure.title('Ввод почты и клик "Восстановить" открывает форму сброса пароля')
    def test_submit_email_opens_reset_password_form(self, driver, registered_user):
        forgot_password_page = ForgotPasswordPage(driver)
        reset_password_page = ResetPasswordPage(driver)

        forgot_password_page.open_page()
        forgot_password_page.set_email(registered_user['email'])
        forgot_password_page.click_restore_button()

        assert reset_password_page.get_save_button_text() == data.SAVE_BUTTON_TEXT

    @allure.title('Клик по иконке показать/скрыть пароль подсвечивает поле')
    def test_click_show_password_icon_highlights_password_field(self, reset_password_page):
        reset_password_page.click_show_password_icon()

        assert reset_password_page.is_password_field_highlighted() is True