import allure

from pages.base_page import BasePageStellarBurgers
from locators.forgot_password_page_locators import ForgotPasswordPageLocators
from precondition.credentials_generators import generator_login_email


class ForgotPasswordPage(BasePageStellarBurgers):
    @allure.step("Ввод email")
    def enter_email_for_forgot_password(self):
        self.add_text_to_element(ForgotPasswordPageLocators.EMAIL_INPUT, generator_login_email())

    @allure.step("Ввод email и клик на восстановить пароль")
    def enter_email_and_click_button_recover(self):
        self.enter_email_for_forgot_password()
        self.move_to_element_and_click(ForgotPasswordPageLocators.BUTTON_FORGOT)
