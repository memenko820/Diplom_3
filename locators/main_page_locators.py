from selenium.webdriver.common.by import By


class MainPageLocators:
    HEADING = (By.XPATH, "//h1[text()='Соберите бургер']")
    INGREDIENT_CARD = (By.XPATH, "//a[@href='/ingredient/{ingredient_id}']")
    INGREDIENT_COUNTER = (By.XPATH, "//a[@href='/ingredient/{ingredient_id}']//p[contains(@class,'counter_counter__num')]")
    CONSTRUCTOR_BASKET = (By.XPATH, "//section[contains(@class,'BurgerConstructor_basket')]")
    PLACE_ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    INGREDIENT_MODAL_HEADING = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]//h2[text()='Детали ингредиента']")
    ORDER_NUMBER = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]//h2[contains(@class, 'Modal_modal__title_shadow')]")