from selenium.webdriver.common.by import By


class ForgotPasswordPageLocators:
    TITLE_PASSWORD_FORGOT_PAGE = By.XPATH, "//h2[text()='Восстановление пароля']"
    EMAIL_INPUT = By.XPATH, "//input[@class='text input__textfield text_type_main-default']"
    BUTTON_FORGOT = By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']"
