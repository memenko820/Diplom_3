import allure
import requests

import data
import helpers


class UsersApi:

    @staticmethod
    @allure.step('Регистрация пользователя')
    def register(payload):
        return requests.post(f'{data.BASE_URL}{data.REGISTER_PATH}', json=payload, timeout=data.REQUEST_TIMEOUT)

    @staticmethod
    @allure.step('Удаление пользователя')
    def delete(token):
        return requests.delete(f'{data.BASE_URL}{data.USER_PATH}',
                               headers=helpers.build_auth_headers(token), timeout=data.REQUEST_TIMEOUT)