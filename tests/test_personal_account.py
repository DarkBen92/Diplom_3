import allure

from conftest import driver, create_user
from data import Data
from pages.header_page import HeaderPage
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage


class TestPersonalAccount:
    @allure.title("Успешный переход по клику на «Личный кабинет».")
    def test_go_to_personal_account(self, driver, create_user):
        driver.get(Data.URL_LOGIN)
        login_page = LoginPage(driver)
        login_page.auth_user(create_user["email"], create_user["password"])

        header_page = HeaderPage(driver)
        header_page.click_personal_account()

        profile_page = ProfilePage(driver)
        assert profile_page.presence_profile_page() == Data.URL_PROFILE

    @allure.title("Успешный переход в раздел «История заказов».")
    def test_go_to_order_history(self, driver, create_user):
        driver.get(Data.URL_LOGIN)
        login_page = LoginPage(driver)
        login_page.auth_user(create_user["email"], create_user["password"])

        header_page = HeaderPage(driver)
        header_page.click_personal_account()

        profile_page = ProfilePage(driver)
        assert profile_page.click_button_order_history() == Data.URL_ORDER_HISTORY

    @allure.title("Успешный выход из аккаунта.")
    def test_log_out_by_button_exit(self, driver, create_user):
        driver.get(Data.URL_LOGIN)
        login_page = LoginPage(driver)
        login_page.auth_user(create_user["email"], create_user["password"])

        header_page = HeaderPage(driver)
        header_page.click_personal_account()

        profile_page = ProfilePage(driver)
        profile_page.click_button_exit()
        assert login_page.presence_feed_page() == Data.URL_LOGIN
