# tests/fixtures.py

import pytest
from selenium import webdriver
import random
import string
from transliterate import translit

@pytest.fixture(scope="session")
def driver():
    # Инициализация драйвера
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.nomoreparties.site")
    #return driver
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def driver_acc():
    # Инициализация драйвера
    driver_acc = webdriver.Chrome()
    driver_acc.get("https://stellarburgers.nomoreparties.site")
    #return driver
    yield driver_acc
    driver_acc.quit()

@pytest.fixture(scope="function")
def driver_reg():
    driver_reg = webdriver.Chrome()
    driver_reg.get("https://stellarburgers.nomoreparties.site/register")
    yield driver_reg
    driver_reg.quit()

@pytest.fixture(scope="function")
def driver_log():
    driver_log = webdriver.Chrome()
    driver_log.get("https://stellarburgers.nomoreparties.site/login")
    yield driver_log
    driver_log.quit()


# # Список русских имен
# names = [
#     "Александр", "Дмитрий", "Павел", "Роман", "Николай",
#     "Виктория", "Оля", "Элеонора", "Марина", "Алиса"
# ]
#
# @pytest.fixture
# def generate_email():
#     # Выбираем случайное имя из списка
#     random_name = random.choice(names)
#     # Транслитерируем имя на латиницу
#     transliterated_name = translit(random_name, 'ru', reversed=True).lower()
#     # Генерация уникальной части email
#     random_string = ''.join(random.choices(string.digits, k=4))
#     email = f"{transliterated_name}{random_string}@yandex.ru"
#     return email, random_name  # возвращаем email и русское имя
#
# # Фикстура для генерации пароля
# @pytest.fixture
# def generate_password():
#     # Генерация случайной длины пароля от 6 до 12 символов
#     length = random.randint(6, 12)
#     # Генерация пароля, состоящего из латинских букв и цифр
#     password = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
#     return password
#
# # Фикстура для объединения generate_email и generate_password в registration_data
# @pytest.fixture
# def registration_data(generate_email, generate_password):
#     email, name = generate_email
#     password = generate_password
#     return {
#         "email": email,
#         "name": name,
#         "password": password
#     }
#
