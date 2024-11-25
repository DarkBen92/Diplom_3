from pages.base_page import BasePageStellarBurgers
from locators.forgot_password_page_locators import ForgotPasswordPageLocators
from locators.reset_password_page_locators import ResetPasswordPageLocators
from precondition.credentials_generators import generator_login_email


class ForgotPasswordPage(BasePageStellarBurgers):
    def enter_email_for_forgot_password(self):
        self.add_text_to_element(ForgotPasswordPageLocators.EMAIL_INPUT, generator_login_email())

    def enter_email_and_click_button_recover(self):
        self.enter_email_for_forgot_password()
        self.click_to_element(ForgotPasswordPageLocators.BUTTON_FORGOT)
        self.find_element_with_wait(ResetPasswordPageLocators.PLACEHOLDER_PASSWORD)
        return self.current_url_page()
