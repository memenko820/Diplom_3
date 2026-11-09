import pytest
from selenium import webdriver

import helpers
from api.ingredients_api import IngredientsApi
from api.orders_api import OrdersApi
from api.users_api import UsersApi
import data
from pages.forgot_password_page import ForgotPasswordPage
from pages.login_page import LoginPage
from pages.reset_password_page import ResetPasswordPage


@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    browsers = {'chrome': webdriver.Chrome,
                'firefox': webdriver.Firefox}
    browser = browsers[request.param]()
    browser.set_window_size(1920, 1080)

    yield browser

    browser.quit()


@pytest.fixture
def registered_user():
    # Пользователь, созданный через API до теста: данные для входа и токен
    payload = helpers.generate_user_payload()
    response = UsersApi.register(payload)
    user = {**payload, 'token': response.json()['accessToken']}

    yield user

    UsersApi.delete(user['token'])


@pytest.fixture
def logged_in_driver(driver, registered_user):
    # Браузер с выполненным входом под пользователем, созданным через API
    login_page = LoginPage(driver)
    login_page.open_page()
    login_page.login(registered_user['email'], registered_user['password'])
    login_page.wait_for_url(data.MAIN_URL)

    return driver


@pytest.fixture
def reset_password_page(driver, registered_user):
    # Страница сброса пароля, открытая через форму восстановления
    forgot_password_page = ForgotPasswordPage(driver)
    forgot_password_page.open_page()
    forgot_password_page.set_email(registered_user['email'])
    forgot_password_page.click_restore_button()

    return ResetPasswordPage(driver)


@pytest.fixture
def ingredients():
    # Список ингредиентов, который отдаёт сервис
    return IngredientsApi.get_ingredients().json()['data']


@pytest.fixture
def sauce(ingredients):
    # Первый соус из списка ингредиентов
    return helpers.find_first_by_type(ingredients, data.INGREDIENT_TYPE_SAUCE)


@pytest.fixture
def bun(ingredients):
    # Первая булка из списка ингредиентов
    return helpers.find_first_by_type(ingredients, data.INGREDIENT_TYPE_BUN)


@pytest.fixture
def ingredient_ids(bun, sauce):
    # Хеши булки и соуса для создания заказа
    return [bun['_id'], sauce['_id']]


@pytest.fixture
def create_order(registered_user, ingredient_ids):
    # Функция создания заказа через API от имени пользователя. возвращает номер заказа
    def _create_order():
        response = OrdersApi.create({'ingredients': ingredient_ids}, registered_user['token'])
        return response.json()['order']['number']

    return _create_order