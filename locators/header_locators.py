from selenium.webdriver.common.by import By


class HeaderLocators:
    CONSTRUCTOR_LINK = (By.XPATH, "//header//a[.//p[text()='Конструктор']]")
    ORDER_FEED_LINK = (By.XPATH, "//header//a[@href='/feed']")
    PERSONAL_ACCOUNT_LINK = (By.XPATH, "//header//a[@href='/account']")