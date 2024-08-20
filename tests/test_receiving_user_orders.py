import allure
import requests

from info import Urls
from info import Text
from info import Ingredients


class TestReceivingUserOrder:
    @allure.description("Получение заказов конкретного пользователя, пользователь авторизован")
    def test_receiving_authorization_user_order(self, create_user):
        response_created, data = create_user
        token = response_created.json()['accessToken']
        headers = {"Content-type": "application/json", "Authorization": f'{token}'}
        ingredients = {"ingredients": [Ingredients.INGREDIENTS_1, Ingredients.INGREDIENTS_2, Ingredients.INGREDIENTS_3]}
        requests.post(Urls.ORDERS, data=ingredients, headers=headers)
        rqst = requests.get(Urls.ORDERS, headers=headers)
        assert rqst.status_code == 200 and Text.TRUE in rqst.text
    @allure.description("Получение заказов конкретного пользователя, пользователь неавторизован")
    def test_receiving_anauthorization_user_order(self):
        rqst = requests.get(Urls.ORDERS)
        assert rqst.status_code == 401 and Text.AUTHORIZED in rqst.text
