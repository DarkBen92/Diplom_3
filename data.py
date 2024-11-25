import allure

from precondition.credentials_generators import generator_login_email, generator_password, generator_name


class Data:
    URL_BASE = "https://stellarburgers.nomoreparties.site"
    URL_FORGOT_PASSWORD = "https://stellarburgers.nomoreparties.site/forgot-password"
    URL_LOGIN = "https://stellarburgers.nomoreparties.site/login"
    URL_RESET_PASSWORD = "https://stellarburgers.nomoreparties.site/reset-password"
    URL_PROFILE = "https://stellarburgers.nomoreparties.site/account/profile"
    URL_ORDER_HISTORY = "https://stellarburgers.nomoreparties.site/account/order-history"


def body_data_user():
    payload = {
        "email": generator_login_email(),
        "password": generator_password(),
        "name": generator_name()
    }
    return payload
