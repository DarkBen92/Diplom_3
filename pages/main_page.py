import time

import allure

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePageStellarBurgers


class MainPage(BasePageStellarBurgers):
    @allure.step("Нахождение на главной странице")
    def presence_main_page(self):
        self.find_element_with_wait(MainPageLocators.TITLE_CONSTRUCTOR)
        return self.current_url_page()

    @allure.step("Открытие окна 'Детали ингредиента'")
    def open_modal_window_details(self):
        self.move_to_element_and_one_click(MainPageLocators.FIRST_BUN)
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

    @allure.step("Создание заказа для получение ИД заказа")
    def create_order_for_text_id_order(self):
        self.move_ingredient_in_basket()
        self.scroll_to_element(MainPageLocators.BUTTON_CREATE_ORDER)
        self.move_to_element_and_click(MainPageLocators.BUTTON_CREATE_ORDER)
        self.find_element_with_wait(MainPageLocators.ID_ORDER)
        return self.text_from_element(MainPageLocators.ID_ORDER)

    @allure.step("Создание заказа")
    def create_order(self):
        self.find_element_with_wait(MainPageLocators.TITLE_CONSTRUCTOR)
        self.move_ingredient_in_basket()
        self.scroll_to_element(MainPageLocators.BUTTON_CREATE_ORDER)
        self.move_to_element_and_click(MainPageLocators.BUTTON_CREATE_ORDER)
        time.sleep(3)
        self.move_to_element_and_click(MainPageLocators.CLOSE_WINDOW_ORDER)
