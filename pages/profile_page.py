import allure

from locators.login_page_locators import LoginPageLocators
from locators.profile_page_locators import ProfilePageLocators
from pages.base_page import BasePageStellarBurgers


class ProfilePage(BasePageStellarBurgers):
    @allure.step("клик на историю заказа")
    def click_button_order_history(self):
        self.move_to_element_and_click(ProfilePageLocators.BUTTON_ORDER_HISTORY_LINK)
        return self.current_url_page()

    @allure.step("клик на кнопку выйти")
    def click_button_exit(self):
        self.move_to_element_and_click(ProfilePageLocators.BUTTON_EXIT)
        self.find_element_with_wait(LoginPageLocators.TITLE_LOGIN)
        return self.current_url_page()

    @allure.step("ид заказ в истории заказа")
    def id_order_in_order_history(self):
        self.move_to_element_and_click(ProfilePageLocators.BUTTON_ORDER_HISTORY_LINK)
        self.find_element_with_wait(ProfilePageLocators.ID_ORDER_HISTORY)
        self.scroll_to_element(ProfilePageLocators.ID_ORDER_HISTORY)
        return self.text_from_element(ProfilePageLocators.ID_ORDER_HISTORY)
