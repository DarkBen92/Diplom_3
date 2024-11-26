import allure

from pages.base_page import BasePageStellarBurgers
from locators.reset_password_page_locators import ResetPasswordPageLocators


class ResetPasswordPage(BasePageStellarBurgers):
    @allure.step("Клик по кнопке отображения пароля")
    def click_button_password_visibility(self):
        self.move_to_element_and_click(ResetPasswordPageLocators.BUTTON_PASSWORD_VISIBILITY)
        return self.find_element_with_wait(ResetPasswordPageLocators.INPUT_STATUS_ACTIVE)

    @allure.step("Подтверждение, что пароль отображается")
    def find_element_active_status_input(self):
        return self.find_element_with_wait(ResetPasswordPageLocators.INPUT_STATUS_ACTIVE)
