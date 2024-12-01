from selenium.webdriver.common.by import By


class LoginPageLocators:
    LINK_FORGOT_PASSWORD = By.XPATH, "//a[text()='Восстановить пароль']"
    EMAIL_INPUT_FIELD = By.XPATH, "//label[text()='Email']/parent::div/input"
    PASSWORD_INPUT_FIELD = By.XPATH, "//label[text()='Пароль']/parent::div/input"
    BUTTON_INPUT = By.XPATH, "//button[contains(text(),'Войти')]"
    TITLE_LOGIN = By.XPATH, "//h2[contains(text(),'Вход')]"
