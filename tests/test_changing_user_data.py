import allure
import requests

from info import Urls
from info import Text

class TestChangingUserData:
    @allure.description("Изменение поля имя, неавторизоавнным пользователем")
    def test_change_name_unauthorized_user(self, create_user):
        response_created, data = create_user
        requests.post(Urls.REGISTER, data=data)
        headers = {"Content-type": "application/json"}
        new_name_value = 'x' + response_created.json()["user"]["name"]
        new_name = {"name": new_name_value}
        rqst = requests.patch(Urls.USER, json=new_name, headers=headers)
        assert rqst.status_code == 401 and Text.AUTHORIZED in rqst.text

    @allure.description("Изменение поля имени, если пользователь авторизован")
    def test_auth_change_name_authorizede_user(self, create_user):
        response_created, data = create_user
        token = response_created.json()['accessToken']
        headers = {"Content-type": "application/json", "Authorization": f'{token}'}
        new_name_value = 'x' + response_created.json()["user"]["name"]
        new_name = {"name": new_name_value}
        rqst = requests.patch(Urls.USER, json=new_name, headers=headers)
        assert rqst.status_code == 200 and rqst.json()['user']['name'] == new_name['name']

    @allure.description("Изменение поля email если пользователь авторизован")
    def test_auth_change_email_authorized_user(self, create_user):
        respons_created, data = create_user
        token = respons_created.json()['accessToken']
        headers = {"Content-type": "application/json", "Authorization": f'{token}'}
        new_email_value = 'x' + respons_created.json()["user"]['email']
        new_email = {"email": new_email_value}
        rqst = requests.patch(Urls.USER, json=new_email, headers=headers)
        assert rqst.status_code == 200 and rqst.json()['user']['email'] == new_email['email']

    @allure.description("Изменение поля пароль, если пользователь авторизован")
    def test_auth_change_password_authorized_user(self, create_user):
        respons_created, data = create_user
        token = respons_created.json()['accessToken']
        headers = {"Content-type": "application/json", "Authorization": f'{token}'}
        new_password_value = 'x' + data["password"]
        new_password = {"password": new_password_value}
        rqst = requests.patch(Urls.USER, json=new_password, headers=headers)
        assert rqst.status_code == 200 and Text.TRUE in rqst.text
