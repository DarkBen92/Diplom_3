import allure
import pytest
from selenium import webdriver

from precondition.setup_order import OrderMethods
from precondition.setup_user import AuthMethods
from data import body_data_user, setup_ingredients


@allure.step("Подготовка driver")
@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == 'chrome':
        driver = webdriver.Chrome()
    else:
        driver = webdriver.Firefox()
    yield driver
    driver.quit()


@allure.step("Создание юзера")
@pytest.fixture
def create_user():
    auth = AuthMethods()
    user_credentials = body_data_user()
    response = auth.register_user(user_credentials)
    yield user_credentials
    token = {"Authorization": response.json()["accessToken"]}
    auth.delete_user(token)


@pytest.fixture
def create_and_token_user():
    auth = AuthMethods()
    user_credentials = body_data_user()
    response = auth.register_user(user_credentials)
    token = {"Authorization": response.json()["accessToken"]}
    yield token, user_credentials
    auth.delete_user(token)


@pytest.fixture
def create_order(create_and_token_user):
    order = OrderMethods()
    response = order.create_order(
        headers=create_and_token_user[0],
        params=setup_ingredients()
    )
    yield str(response.json()["order"]["number"])

