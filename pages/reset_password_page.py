from pages.base_page import BasePageStellarBurgers
from locators.reset_password_page_locators import ResetPasswordPageLocators


class ResetPasswordPage(BasePageStellarBurgers):
    def click_button_password_visibility(self):
        self.click_to_element(ResetPasswordPageLocators.BUTTON_PASSWORD_VISIBILITY)
        self.find_element_with_wait(ResetPasswordPageLocators.INPUT_STATUS_ACTIVE)
        return ResetPasswordPageLocators.INPUT_STATUS_ACTIVE

    def find_element_not_active_field(self):
        self.find_element_with_wait(ResetPasswordPageLocators.INPUT_STATUS_NOT_ACTIVE)
