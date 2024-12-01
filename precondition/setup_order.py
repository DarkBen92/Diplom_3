import allure
import requests

from data import Data


class OrderMethods:
    @allure.step("Создание заказа")
    def create_order(self, headers, params):
        response = requests.post(f"{Data.URL_BASE}api/orders/", headers=headers, json=params)
        return response
