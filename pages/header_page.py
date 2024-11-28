import allure

from locators.header_page_locators import HeaderPageLocators
from pages.base_page import BasePageStellarBurgers


class HeaderPage(BasePageStellarBurgers):
    @allure.step("Клик на 'Лента Заказа'")
    def click_order_feed(self):
        self.scroll_to_element(HeaderPageLocators.ORDER_FEED)
        self.move_to_element_and_click(HeaderPageLocators.ORDER_FEED)

    @allure.step("Клик на 'Конструктор'")
    def click_constructor(self):
        self.scroll_to_element(HeaderPageLocators.CONSTRUCTOR)
        self.move_to_element_and_click(HeaderPageLocators.CONSTRUCTOR)

    @allure.step("Клик по 'Личный кабинет'")
    def click_personal_account(self):
        self.scroll_to_element(HeaderPageLocators.PERSONAL_ACCOUNT)
        self.move_to_element_and_click(HeaderPageLocators.PERSONAL_ACCOUNT)
