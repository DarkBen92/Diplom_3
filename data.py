from precondition.credentials_generators import generator_login_email, generator_password, generator_name


class Data:
    URL_BASE = "https://stellarburgers.nomoreparties.site/"
    URL_FORGOT_PASSWORD = "https://stellarburgers.nomoreparties.site/forgot-password"
    URL_LOGIN = "https://stellarburgers.nomoreparties.site/login"
    URL_RESET_PASSWORD = "https://stellarburgers.nomoreparties.site/reset-password"
    URL_PROFILE = "https://stellarburgers.nomoreparties.site/account/profile"
    URL_ORDER_HISTORY = "https://stellarburgers.nomoreparties.site/account/order-history"
    URL_FEED = "https://stellarburgers.nomoreparties.site/feed"

    COUNTER_BUN = "2"
    ORDER_ID = "9999"


def body_data_user():
    payload = {
        "email": generator_login_email(),
        "password": generator_password(),
        "name": generator_name()
    }
    return payload


def setup_ingredients():
    payload = {
        "ingredients": [
            "61c0c5a71d1f82001bdaaa71",
            "61c0c5a71d1f82001bdaaa78"
        ]
    }
    return payload
