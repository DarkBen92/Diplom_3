from conftest import driver
from data import Data


from pages.login_page import LoginPage
from pages.forgot_password_page import ForgotPasswordPage
from pages.reset_password_page import ResetPasswordPage
from locators.reset_password_page_locators import ResetPasswordPageLocators


class TestForgotPassword:
    def test_go_to_forgot_password(self, driver):
        driver.get(Data.URL_LOGIN)
        login_page = LoginPage(driver)
        assert login_page.go_to_forgot_password_page() == Data.URL_FORGOT_PASSWORD

    def test_restore_by_email(self, driver):
        driver.get(Data.URL_FORGOT_PASSWORD)
        forgot_password_page = ForgotPasswordPage(driver)
        assert forgot_password_page.enter_email_and_click_button_recover() == Data.URL_RESET_PASSWORD

    def test_field_password_active(self, driver):
        driver.get(Data.URL_FORGOT_PASSWORD)
        forgot_password_page = ForgotPasswordPage(driver)
        forgot_password_page.enter_email_and_click_button_recover()
        reset_password_page = ResetPasswordPage(driver)
        assert reset_password_page.click_button_password_visibility() != ResetPasswordPageLocators.INPUT_STATUS_NOT_ACTIVE
