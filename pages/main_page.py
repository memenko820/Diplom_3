import allure

import data
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage

# Имитация HTML5-перетаскивания
DRAG_AND_DROP_SCRIPT = '''
const source = arguments[0];
const target = arguments[1];
const dataTransfer = new DataTransfer();
for (const type of ['dragstart', 'dragenter', 'dragover', 'drop', 'dragend']) {
    const element = (type === 'dragstart' || type === 'dragend') ? source : target;
    element.dispatchEvent(new DragEvent(type, {bubbles: true, cancelable: true, dataTransfer: dataTransfer}));
}
'''


class MainPage(BasePage):

    @allure.step('Открыть главную страницу')
    def open_page(self):
        self.open_url(data.MAIN_URL)

    def get_heading_text(self):
        return self.get_text(MainPageLocators.HEADING)

    @allure.step('Добавить ингредиент в конструктор перетаскиванием')
    def add_ingredient_to_constructor(self, ingredient_id):
        card_locator = self.format_locator(MainPageLocators.INGREDIENT_CARD, ingredient_id=ingredient_id)
        source = self.wait_for_visible(card_locator)
        target = self.wait_for_visible(MainPageLocators.CONSTRUCTOR_BASKET)
        self.driver.execute_script(DRAG_AND_DROP_SCRIPT, source, target)

    def is_ingredient_counter_equal(self, ingredient_id, value):
        counter_locator = self.format_locator(MainPageLocators.INGREDIENT_COUNTER, ingredient_id=ingredient_id)
        return self.is_text_equal(counter_locator, str(value))

    @allure.step('Нажать на ингредиент')
    def click_ingredient(self, ingredient_id):
        self.click(self.format_locator(MainPageLocators.INGREDIENT_CARD, ingredient_id=ingredient_id))

    def get_ingredient_modal_heading_text(self):
        return self.get_text(MainPageLocators.INGREDIENT_MODAL_HEADING)

    @allure.step('Нажать "Оформить заказ"')
    def click_place_order_button(self):
        self.click(MainPageLocators.PLACE_ORDER_BUTTON)

    def is_order_number_displayed(self):
        return self.is_condition_met(lambda driver: (
            driver.find_element(*MainPageLocators.ORDER_NUMBER).text.isdigit()
            and driver.find_element(*MainPageLocators.ORDER_NUMBER).text != data.ORDER_NUMBER_PLACEHOLDER))