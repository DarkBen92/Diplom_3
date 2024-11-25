from selenium.webdriver.common.by import By


class ProfilePageLocators:
    BUTTON_PROFILE_LINK = By.XPATH, "//a[contains(text(),'Профиль')]"
    BUTTON_ORDER_HISTORY_LINK = By.XPATH, "//a[contains(text(),'История заказов')]"
    BUTTON_EXIT = By.XPATH, "//button[text()='Выход']"
