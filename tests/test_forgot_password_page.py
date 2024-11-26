import allure

from conftest import driver
from data import Data


from pages.login_page import LoginPage
from pages.forgot_password_page import ForgotPasswordPage
from pages.reset_password_page import ResetPasswordPage


class TestForgotPassword:
    @allure.title("Успешный переход на страницу восстановления пароля по кнопке «Восстановить пароль».")
    def test_go_to_forgot_password(self, driver):
        driver.get(Data.URL_LOGIN)
        login_page = LoginPage(driver)
        assert login_page.go_to_forgot_password_page() == Data.URL_FORGOT_PASSWORD

    @allure.title("Успешный ввод почты и клик по кнопке «Восстановить».")
    def test_restore_by_email(self, driver):
        driver.get(Data.URL_FORGOT_PASSWORD)
        forgot_password_page = ForgotPasswordPage(driver)
        assert forgot_password_page.enter_email_and_click_button_recover() == Data.URL_RESET_PASSWORD

    @allure.title("Успешный клик по кнопке показать/скрыть пароль делает поле активны.")
    def test_field_password_active(self, driver):
        driver.get(Data.URL_FORGOT_PASSWORD)
        forgot_password_page = ForgotPasswordPage(driver)
        forgot_password_page.enter_email_and_click_button_recover()
        reset_password_page = ResetPasswordPage(driver)
        assert reset_password_page.click_button_password_visibility() == reset_password_page.find_element_active_status_input()
