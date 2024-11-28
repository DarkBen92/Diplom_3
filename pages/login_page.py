import allure

from pages.base_page import BasePageStellarBurgers
from locators.login_page_locators import LoginPageLocators


class LoginPage(BasePageStellarBurgers):
    @allure.step("Клик на ссылку Восстановить пароль")
    def click_to_link_forgot_password(self):
        self.move_to_element_and_click(LoginPageLocators.LINK_FORGOT_PASSWORD)

    @allure.step("Переход на страницу востановления пароля")
    def go_to_forgot_password_page(self):
        self.click_to_link_forgot_password()
        return self.current_url_page()

    @allure.step("Нахождение на странице авторизации")
    def presence_feed_page(self):
        self.find_element_with_wait(LoginPageLocators.TITLE_LOGIN)
        return self.current_url_page()

    @allure.step("Получить email")
    def set_email_field(self, email):
        self.add_text_to_element(LoginPageLocators.EMAIL_INPUT_FIELD, email)

    @allure.step("Получить пароль")
    def set_password_field(self, password):
        self.add_text_to_element(LoginPageLocators.PASSWORD_INPUT_FIELD, password)

    @allure.step("Авторизация юзера")
    def auth_user(self, email, password):
        self.set_email_field(email)
        self.set_password_field(password)
        self.move_to_element_and_click(LoginPageLocators.BUTTON_INPUT)
        return self.current_url_page()
