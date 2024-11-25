import allure
import requests

from data import Data


class AuthMethods:
    @allure.step("Регистрация пользователя")
    def register_user(self, params):
        response = requests.post(f"{Data.URL_BASE}/api/auth/register", json=params)
        return response

    @allure.step("Удаление пользователя")
    def delete_user(self, headers):
        response = requests.delete(f"{Data.URL_BASE}/api/auth/user", headers=headers)
        return response
