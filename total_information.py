import allure
import random
import string


class TotalInformation:

    @allure.step('Генерируем данные для пользователя')
    def register_new_user_and_return_login_password(self):
        def generate_random_string(length):
            letters = string.ascii_lowercase
            random_string = ''.join(random.choice(letters) for i in range(length))
            return random_string

        # генерируем логин, пароль и имя пользователя
        email = generate_random_string(6) + '@yandex.ru'
        password = generate_random_string(10)
        name = generate_random_string(10)

        # собираем тело запроса
        payload = {
            "email": email,
            "password": password,
            "name": name
        }

        return payload