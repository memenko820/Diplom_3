import random
import string

import data


def generate_random_string(length):
    # Строка из букв нижнего регистра заданной длины
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))


def generate_email():
    # Уникальный email для тестового пользователя
    return f'{generate_random_string(10)}@yandex.ru'


def generate_user_payload():
    # Данные для регистрации нового пользователя
    return {
        'email': generate_email(),
        'password': generate_random_string(10),
        'name': generate_random_string(10),
    }


def build_auth_headers(token):
    # Заголовки с токеном; без токена заголовков авторизации нет
    return {data.AUTH_HEADER: token} if token else {}


def find_first_by_type(ingredients, ingredient_type):
    # Первый ингредиент указанного типа из списка, который отдаёт API
    return next(item for item in ingredients if item['type'] == ingredient_type)


def format_order_number(number):
    # Номер заказа в формате ленты: шесть цифр с ведущими нулями
    return str(number).zfill(6)