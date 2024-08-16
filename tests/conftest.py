import pytest
import requests

from info import Urls
from total_information import TotalInformation

@pytest.fixture(scope='function')
def create_user():
    details = TotalInformation()
    data = details.register_new_user_and_return_login_password()
    response_post = requests.post(Urls.REGISTER, data=data)
    token = response_post.json()['accessToken']
    headers = {"Content-type": "application/json", "Authorization": f'{token}'}
    yield response_post, data
    requests.delete(Urls.INFO_USER, headers=headers)