from selenium.webdriver.common.by import By


class BasePageLocators:
    MODAL_OVERLAY = (By.XPATH, "//div[contains(@class, 'Modal_modal_overlay')]")
    OPENED_MODAL = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]")
    MODAL_CLOSE_BUTTON = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]//button[contains(@class, 'Modal_modal__close')]")