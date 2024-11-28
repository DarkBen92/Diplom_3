import allure

from pages.base_page import BasePageStellarBurgers
from locators.feed_page_locators import FeedPageLocators


class FeedPage(BasePageStellarBurgers):
    @allure.step("Нахождение в ленте заказов")
    def presence_feed_page(self):
        self.find_element_with_wait(FeedPageLocators.TITLE_FEED)
        return self.current_url_page()

    @allure.step("Открытие первого заказа")
    def open_first_order(self):
        self.move_to_element_and_click(FeedPageLocators.FIRST_ORDER_IN_LIST)
        self.find_element_with_wait(FeedPageLocators.MODAL_WINDOW_ORDER)
        return self.text_from_element(FeedPageLocators.TEXT_MODAL_WINDOW_ORDER)

    @allure.step("Заказ пользователя")
    def user_order(self):
        return self.text_from_element(FeedPageLocators.ID_ORDER)

    @allure.step("Выполнено за всё время")
    def completed_all_the_time(self):
        self.presence_feed_page()
        return self.text_from_element(FeedPageLocators.NUMBER_ALL_TIME)

    @allure.step("Выполнено за сегодня")
    def completed_today(self):
        self.presence_feed_page()
        return self.text_from_element(FeedPageLocators.NUMBER_TODAY)

    @allure.step("Номер заказа")
    def number_order(self):
        return self.text_from_element(FeedPageLocators.NUMBER_ORDER)
