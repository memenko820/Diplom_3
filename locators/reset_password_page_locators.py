from selenium.webdriver.common.by import By


class ResetPasswordPageLocators:
    SHOW_PASSWORD_ICON = (By.XPATH, "//label[text()='Пароль']/following-sibling::div[contains(@class,'input__icon-action')]")
    PASSWORD_FIELD_ACTIVE = (By.XPATH, "//label[text()='Пароль']/parent::div[contains(@class,'input_status_active')]")
    SAVE_BUTTON = (By.XPATH, "//button[text()='Сохранить']")