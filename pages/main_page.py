from locators.main_page_locators import MainPageLocators
from locators.profile_page_locators import ProfilePageLocators
from pages.base_page import BasePageStellarBurgers


class MainPage(BasePageStellarBurgers):
    def click_personal_account(self):
        self.scroll_to_element(MainPageLocators.PERSONAL_ACCOUNT)
        self.move_to_element_and_click(MainPageLocators.PERSONAL_ACCOUNT)
        self.find_element_with_wait(ProfilePageLocators.BUTTON_PROFILE_LINK)
        return self.current_url_page()
