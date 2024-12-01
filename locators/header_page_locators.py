from selenium.webdriver.common.by import By


class HeaderPageLocators:
    CONSTRUCTOR = By.XPATH, "//p[contains(text(),'Конструктор')]"
    PERSONAL_ACCOUNT = By.XPATH, "//p[contains(text(),'Личный Кабинет')]"
    ORDER_FEED = By.XPATH, "//p[contains(text(),'Лента Заказов')]"
