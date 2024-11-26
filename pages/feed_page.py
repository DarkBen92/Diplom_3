import allure

from locators.header_page_locators import HeaderPageLocators
from locators.main_page_locators import MainPageLocators
from locators.profile_page_locators import ProfilePageLocators
from pages.base_page import BasePageStellarBurgers
from locators.feed_page_locators import FeedPageLocators


class FeedPage(BasePageStellarBurgers):
    @allure.step("Открытие первого заказа")
    def open_first_order(self):
        self.move_to_element_and_click(FeedPageLocators.FIRST_ORDER_IN_LIST)
        self.find_element_with_wait(FeedPageLocators.MODAL_WINDOW_ORDER)
        return self.text_from_element(FeedPageLocators.TEXT_MODAL_WINDOW_ORDER)

    @allure.step("Заказ пользователя")
    def user_order(self):
        self.scroll_to_element(ProfilePageLocators.ID_ORDER_HISTORY)
        return self.text_from_element(FeedPageLocators.ID_ORDER)

    @allure.step("Выполнено за всё время")
    def completed_all_the_time(self):
        self.scroll_to_element(HeaderPageLocators.ORDER_FEED)
        self.move_to_element_and_click(HeaderPageLocators.ORDER_FEED)
        self.find_element_with_wait(FeedPageLocators.TITLE_FEED)
        return self.text_from_element(FeedPageLocators.NUMBER_ALL_TIME)

    def change_number(self, new_number, first_number) -> bool:
        if new_number > first_number:
            return True
        else:
            return False

    @allure.step("Создание заказа для нового номера заказа")
    def create_order_for_new_number(self):
        self.scroll_to_element(HeaderPageLocators.CONSTRUCTOR)
        self.move_to_element_and_click(HeaderPageLocators.CONSTRUCTOR)
        self.find_element_with_wait(MainPageLocators.TITLE_CONSTRUCTOR)
        self.drag_and_drop_element(MainPageLocators.FIRST_BUN, MainPageLocators.BASKET)
        self.scroll_to_element(MainPageLocators.BUTTON_CREATE_ORDER)
        self.move_to_element_and_click(MainPageLocators.BUTTON_CREATE_ORDER)
        self.find_element_with_wait(MainPageLocators.CLOSE_WINDOW_ORDER)
        self.move_to_element_and_click(MainPageLocators.CLOSE_WINDOW_ORDER)

    @allure.step("Выполнено за сегодня")
    def completed_today(self):
        self.scroll_to_element(HeaderPageLocators.ORDER_FEED)
        self.move_to_element_and_click(HeaderPageLocators.ORDER_FEED)
        self.find_element_with_wait(FeedPageLocators.TITLE_FEED)
        return self.text_from_element(FeedPageLocators.NUMBER_TODAY)

    @allure.step("Номер заказа")
    def number_order(self):
        return self.text_from_element(FeedPageLocators.NUMBER_ORDER)
