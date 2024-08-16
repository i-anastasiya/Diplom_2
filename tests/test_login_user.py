import allure
import requests

from info import Urls
from info import Text
from total_information import TotalInformation

class TestLoginUser:
    @allure.description("Логин под существующим пользователем")
    def test_login_already_user(self, create_user):
        response_created, data = create_user
        del data["name"]
        response = requests.post(Urls.LOGIN, data=data)
        assert response.status_code == 200 and Text.TRUE in resp.text
    @allure.description("Логин с неверным логином и паролем")
    def test_login_wrong_password_and_login(self):
        details = TotalInformation()
        user_data = details.register_new_user_and_return_login_password()
        del user_data["name"]
        response = requests.post(Urls.LOGIN, data=user_data)
        assert response.status_code == 401 and Text.INCORRECT
