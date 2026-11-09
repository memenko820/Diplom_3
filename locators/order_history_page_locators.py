from selenium.webdriver.common.by import By


class OrderHistoryPageLocators:
    FIRST_ORDER_NUMBER = (
        By.XPATH,
        "(//ul[contains(@class, 'OrderHistory_profileList')]//a[contains(@class, 'OrderHistory_link')]"
        "//p[starts-with(normalize-space(), '#')])[1]")