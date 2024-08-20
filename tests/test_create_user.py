import allure
import requests

from info import Urls
from info import Text
from total_information import TotalInformation


class TestCreateUser:
    @allure.description('Cоздать уникального пользователя')
    def test_create_user(self, create_user):
        response_created, data = create_user
        assert response_created.status_code == 200
        assert Text.TRUE in response_created.text

    @allure.description("Создать пользователя, который уже зарегистрирован")
    def test_create_user_already_registered(self, create_user):
        response_created, data = create_user
        response = requests.post(Urls.REGISTER, data=data)
        assert response.status_code == 403 and Text.FALSE

    @allure.description("Создать пользователя и не заполнить одно из обязательных полей")
    def test_create_user_no_required_field(self):
        details = TotalInformation()
        rqst = details.register_new_user_and_return_login_password()
        rqst['name'] = ''
        response = requests.post(Urls.REGISTER, data=rqst)
        assert response.status_code == 403 and Text.ALREADY_EXISTS
