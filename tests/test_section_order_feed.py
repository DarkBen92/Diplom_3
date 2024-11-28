import allure

from data import Data
from helpers import change_number
from pages.feed_page import FeedPage
from conftest import driver, create_order, create_and_token_user
from pages.header_page import HeaderPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.profile_page import ProfilePage


class TestSectionOrderFeed:
    @allure.title("Успешное открытие окна с деталями")
    def test_open_window_order_details(self, driver):
        driver.get(Data.URL_FEED)
        feed_page = FeedPage(driver)
        assert feed_page.open_first_order() == "Cостав"

    @allure.title("Успешное отображение заказа")
    def test_order_user_displayed_order_feed(self, driver, create_and_token_user, create_order):
        driver.get(Data.URL_LOGIN)
        login_page = LoginPage(driver)
        login_page.auth_user(create_and_token_user[1]["email"], create_and_token_user[1]["password"])
        header_page = HeaderPage(driver)
        header_page.click_personal_account()
        profile_page = ProfilePage(driver)
        number_order = profile_page.id_order_in_order_history()
        header_page.click_order_feed()
        feed_page = FeedPage(driver)
        assert feed_page.user_order() == number_order

    @allure.title("Увеличение счетчика Выполнено за всё время")
    def test_order_completed_all_the_time(self, driver, create_and_token_user):
        driver.get(Data.URL_LOGIN)
        login_page = LoginPage(driver)
        login_page.auth_user(create_and_token_user[1]["email"], create_and_token_user[1]["password"])
        header_page = HeaderPage(driver)
        header_page.click_order_feed()
        feed_page = FeedPage(driver)
        first_number = feed_page.completed_all_the_time()
        header_page.click_constructor()
        main_page = MainPage(driver)
        main_page.create_order()
        header_page.click_order_feed()
        new_number = feed_page.completed_all_the_time()
        assert change_number(new_number, first_number) == True

    @allure.title("Увеличение счетчика Выполнено за сегодня")
    def test_order_completed_today(self, driver, create_and_token_user):
        driver.get(Data.URL_LOGIN)
        login_page = LoginPage(driver)
        login_page.auth_user(create_and_token_user[1]["email"], create_and_token_user[1]["password"])
        header_page = HeaderPage(driver)
        header_page.click_order_feed()
        feed_page = FeedPage(driver)
        first_number = feed_page.completed_today()
        header_page.click_constructor()
        main_page = MainPage(driver)
        main_page.create_order()
        header_page.click_order_feed()
        new_number = feed_page.completed_today()
        assert change_number(new_number, first_number) == True

    @allure.title("Появление номера заказа В работе")
    def test_number_at_work(self, driver, create_and_token_user, create_order):
        driver.get(Data.URL_LOGIN)
        login_page = LoginPage(driver)
        login_page.auth_user(create_and_token_user[1]["email"], create_and_token_user[1]["password"])
        header_page = HeaderPage(driver)
        header_page.click_order_feed()
        feed_page = FeedPage(driver)
        assert feed_page.number_order() == f"0{create_order}"
