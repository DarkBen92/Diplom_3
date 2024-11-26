import allure

from locators.header_page_locators import HeaderPageLocators
from locators.profile_page_locators import ProfilePageLocators
from locators.feed_page_locators import FeedPageLocators
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePageStellarBurgers


class MainPage(BasePageStellarBurgers):
    @allure.step("Клик по 'Личный кабинет'")
    def click_personal_account(self):
        self.scroll_to_element(HeaderPageLocators.PERSONAL_ACCOUNT)
        self.move_to_element_and_click(HeaderPageLocators.PERSONAL_ACCOUNT)
        self.find_element_with_wait(ProfilePageLocators.BUTTON_PROFILE_LINK)
        return self.current_url_page()

    @allure.step("Клик по 'Лента заказов'")
    def click_order_feed(self):
        self.scroll_to_element(HeaderPageLocators.ORDER_FEED)
        self.move_to_element_and_click(HeaderPageLocators.ORDER_FEED)
        self.find_element_with_wait(FeedPageLocators.TITLE_FEED)
        return self.current_url_page()

    @allure.step("Открытие окна 'Детали ингредиента'")
    def open_modal_window_details(self):
        self.move_to_element_and_click(MainPageLocators.FIRST_BUN)
        self.find_element_with_wait(MainPageLocators.MODAL_WINDOW_DETAILS)
        return self.text_from_element(MainPageLocators.TITLE_MODAL_WINDOW_DETAILS)

    @allure.step("Закрытие окна 'Детали ингредиента'")
    def close_modal_window_details(self):
        self.move_to_element_and_click(MainPageLocators.BUTTON_CLOSE_MODAL_WINDOW_DETAILS)
        return self.find_element_with_wait(MainPageLocators.CLOSE_MODAL_WINDOW_DETAILS)

    @allure.step("Подтверждение, что окно закрыто 'Детали ингредиента'")
    def find_element_close_modal_window_details(self):
        return self.find_element_with_wait(MainPageLocators.CLOSE_MODAL_WINDOW_DETAILS)

    @allure.step("Добавление ингредиента в корзину")
    def move_ingredient_in_basket(self):
        self.drag_and_drop_element(MainPageLocators.FIRST_BUN, MainPageLocators.BASKET)
        self.find_element_with_wait(MainPageLocators.COUNTER)
        return self.text_from_element(MainPageLocators.COUNTER)

    @allure.step("Попытка создание заказа")
    def create_order(self):
        self.move_ingredient_in_basket()
        self.scroll_to_element(MainPageLocators.BUTTON_CREATE_ORDER)
        self.move_to_element_and_click(MainPageLocators.BUTTON_CREATE_ORDER)
        self.find_element_with_wait(MainPageLocators.ID_ORDER)
        return self.text_from_element(MainPageLocators.ID_ORDER)
