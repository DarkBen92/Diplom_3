from locators.login_page_locators import LoginPageLocators
from locators.profile_page_locators import ProfilePageLocators
from pages.base_page import BasePageStellarBurgers


class ProfilePage(BasePageStellarBurgers):
    def click_button_order_history(self):
        self.move_to_element_and_click(ProfilePageLocators.BUTTON_ORDER_HISTORY_LINK)
        return self.current_url_page()

    def click_button_exit(self):
        self.move_to_element_and_click(ProfilePageLocators.BUTTON_EXIT)
        self.find_element_with_wait(LoginPageLocators.TITLE_LOGIN)
        return self.current_url_page()
