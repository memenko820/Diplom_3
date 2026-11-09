# Базовый URL сервиса
BASE_URL = 'https://qa-stellarburgers.education-services.ru'
# URL после авторизации
MAIN_URL = f'{BASE_URL}/'
FEED_URL = f'{BASE_URL}/feed'

# Страницы приложения
LOGIN_URL = f'{BASE_URL}/login'
FORGOT_PASSWORD_URL = f'{BASE_URL}/forgot-password'

# Таймаут запросов, секунды
REQUEST_TIMEOUT = 30
# Время ожидания элементов, секунды
WAIT_TIMEOUT = 10

# Пути ручек
REGISTER_PATH = '/api/auth/register'
USER_PATH = '/api/auth/user'
INGREDIENTS_PATH = '/api/ingredients'
ORDERS_PATH = '/api/orders'

# Заголовок авторизации
AUTH_HEADER = 'Authorization'
# Заголовки страниц
FORGOT_PASSWORD_HEADING = 'Восстановление пароля'

# Тексты элементов
LOGIN_HEADING = 'Вход'
SAVE_BUTTON_TEXT = 'Сохранить'
PROFILE_MENU_ITEM_TEXT = 'Профиль'
ORDER_HISTORY_MENU_ITEM_TEXT = 'История заказов'
CONSTRUCTOR_HEADING = 'Соберите бургер'
ORDER_FEED_HEADING = 'Лента заказов'
INGREDIENT_MODAL_HEADING = 'Детали ингредиента'

# Типы ингредиентов в ответе API
INGREDIENT_TYPE_BUN = 'bun'
INGREDIENT_TYPE_SAUCE = 'sauce'

# Номер, который окно заказа показывает, пока сервер не вернул настоящий
ORDER_NUMBER_PLACEHOLDER = '9999'