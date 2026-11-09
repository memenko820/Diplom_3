from selenium.webdriver.common.by import By


class OrderFeedPageLocators:
    HEADING = (By.XPATH, "//h1[text()='Лента заказов']")
    ORDER_CARD = (By.XPATH, "//a[contains(@class, 'OrderHistory_link')][.//p[normalize-space(text())='{order_number}']]")
    TOTAL_ORDERS_COUNTER = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
    TODAY_ORDERS_COUNTER = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")
    IN_PROGRESS_ORDER = (
        By.XPATH,
        "//ul[contains(@class, 'OrderFeed_orderList') and not(contains(@class, 'OrderFeed_orderListReady'))]"
        "//li[normalize-space(.)='{order_number}']")
    FIRST_ORDER_CARD = (By.XPATH, "(//a[contains(@class, 'OrderHistory_link')])[1]")
    ORDER_MODAL_CONTENT = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]//div[contains(@class, 'Modal_orderBox')]")