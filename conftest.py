import pytest
from selenium import webdriver

from precondition.setup_user import AuthMethods
from data import body_data_user


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == 'chrome':
        driver = webdriver.Chrome()
    else:
        driver = webdriver.Firefox()
    yield driver
    driver.quit()


@pytest.fixture
def create_user():
    auth = AuthMethods()
    user_credentials = body_data_user()
    response = auth.register_user(user_credentials)
    yield user_credentials
    token = {"Authorization": response.json()["accessToken"]}
    auth.delete_user(token)


