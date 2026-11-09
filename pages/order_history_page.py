from locators.order_history_page_locators import OrderHistoryPageLocators
from pages.profile_page import ProfilePage


class OrderHistoryPage(ProfilePage):

    def get_first_order_number(self):
        return self.get_text(OrderHistoryPageLocators.FIRST_ORDER_NUMBER)