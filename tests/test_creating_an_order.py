import allure
import requests

from info import Urls
from info import Text
from info import Ingredients


class TestCreateAnOrder:
    @allure.description("Создание заказа с атворизацией и ингредиентами")
    def test_authorization_create_order_with_ingredients(self, create_user):
        response_created, data = create_user
        del data["name"]
        requests.post(Urls.LOGIN, data=data)
        ingredients = {"ingredients": [Ingredients.INGREDIENTS_1, Ingredients.INGREDIENTS_2, Ingredients.INGREDIENTS_3]}
        rqst = requests.post(Urls.ORDERS, data=ingredients)
        assert rqst.status_code == 200 and Text.TRUE in rqst.text
    @allure.description("Создание заказа без авторизации")
    def test_no_authorization_create_order(self):
        rqst = requests.post(Urls.ORDERS)
        assert rqst.status_code == 400 and Text.REQUIRED_DATA in rqst.text
    @allure.description("Создание заказа с авторизацией и без ингридиентов")
    def test_auth_create_order_with_ingredients(self, create_user):
        response_created, data = create_user
        del data["name"]
        requests.post(Urls.LOGIN, data=data)
        ingredients = {"ingredients": ""}
        rqst = requests.post(Urls.ORDERS, data=ingredients)
        assert rqst.status_code == 400 and Text.REQUIRED_DATA in rqst.text
    @allure.description("Создание заказ без авторизации и с неверным хешем ингредиентов")
    def test_no_auth_create_order_hash(self):
        ingredients = {"ingredients": [Ingredients.INGREDIENTS_4, Ingredients.INGREDIENTS_3]}
        rqst = requests.post(Urls.ORDERS, data=ingredients)
        assert rqst.status_code == 500 and Text.Server_Error in rqst.text
