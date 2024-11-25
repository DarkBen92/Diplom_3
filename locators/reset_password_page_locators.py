from selenium.webdriver.common.by import By


class ResetPasswordPageLocators:
    PLACEHOLDER_PASSWORD = By.XPATH, "//label[text()='Пароль']"
    BUTTON_PASSWORD_VISIBILITY = By.XPATH, "//div[@class='input__icon input__icon-action']//*[name()='svg']"
    INPUT_STATUS_ACTIVE = By.XPATH, "//div[@class='input pr-6 pl-6 input_type_text input_size_default input_status_active']"
    INPUT_STATUS_NOT_ACTIVE = By.XPATH, "//div[@class='input pr-6 pl-6 input_type_password input_size_default']"
