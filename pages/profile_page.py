import allure

from locators.profile_page_locators import ProfilePageLocators
from pages.base_page import BasePage


class ProfilePage(BasePage):

    @allure.step('Нажать "История заказов"')
    def click_order_history_link(self):
        self.click(ProfilePageLocators.ORDER_HISTORY_LINK)

    @allure.step('Нажать "Выход"')
    def click_logout_button(self):
        self.click(ProfilePageLocators.LOGOUT_BUTTON)

    def get_active_profile_link_text(self):
        return self.get_text(ProfilePageLocators.PROFILE_LINK_ACTIVE)

    def get_active_order_history_link_text(self):
        return self.get_text(ProfilePageLocators.ORDER_HISTORY_LINK_ACTIVE)