import time

import allure

from data import Data
from pages.feed_page import FeedPage
from pages.header_page import HeaderPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from conftest import driver, create_user


class TestMainPage:
    @allure.title("Успешный переход по клику на «Конструктор».")
    def test_go_to_constructor_page(self, driver):
        driver.get(Data.URL_LOGIN)
        header_page = HeaderPage(driver)
        header_page.click_constructor()
        main_page = MainPage(driver)
        assert main_page.presence_main_page() == Data.URL_BASE

    @allure.title("Успешный переход по клику на «Лента заказов».")
    def test_go_to_order_feed_page(self, driver):
        driver.get(Data.URL_BASE)
        header_page = HeaderPage(driver)
        header_page.click_order_feed()
        feed_page = FeedPage(driver)
        assert feed_page.presence_feed_page() == Data.URL_FEED

    @allure.title("Появление модального окна с деталями.")
    def test_advent_modal_window_with_details(self, driver):
        driver.get(Data.URL_BASE)
        main_page = MainPage(driver)
        assert main_page.open_modal_window_details() == "Детали ингредиента"

    @allure.title("Успешное закрытие модального окна с деталями.")
    def test_close_modal_window_with_details(self, driver):
        driver.get(Data.URL_BASE)
        main_page = MainPage(driver)
        main_page.open_modal_window_details()
        assert main_page.close_modal_window_details() == main_page.find_element_close_modal_window_details()

    @allure.title("Отображение увеличенного каунтера добавленного ингредиента.")
    def test_add_ingredient_increase_counter(self, driver):
        driver.get(Data.URL_BASE)
        main_page = MainPage(driver)
        assert main_page.move_ingredient_in_basket() == Data.COUNTER_BUN

    @allure.title("Успешное оформление заказа залогиненным пользователем.")
    def test_create_order(self, driver, create_user):
        driver.get(Data.URL_LOGIN)
        login_page = LoginPage(driver)
        login_page.auth_user(create_user["email"], create_user["password"])
        main_page = MainPage(driver)
        assert main_page.create_order_for_text_id_order() == Data.ORDER_ID
