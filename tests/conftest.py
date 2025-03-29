# tests/fixtures.py
import pytest
from selenium import webdriver
import random
import string
from transliterate import translit
from ..url_holder import *
from ..data_generator import *
import sys
sys.path.append('C:/Users/slipk/PycharmProjects/SprintUI5')
@pytest.fixture(scope="session")
def driver():
    # Инициализация драйвера
    driver = webdriver.Chrome()
    driver.get(url_home)
    #return driver
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def driver_acc():
    # Инициализация драйвера
    driver_acc = webdriver.Chrome()
    driver_acc.get(url_home)
    #return driver
    yield driver_acc
    driver_acc.quit()

@pytest.fixture(scope="function")
def driver_reg():
    driver_reg = webdriver.Chrome()
    driver_reg.get(url_reg_form)
    yield driver_reg
    driver_reg.quit()

@pytest.fixture(scope="function")
def driver_log():
    driver_log = webdriver.Chrome()
    driver_log.get(url_login)
    yield driver_log
    driver_log.quit()

@pytest.fixture
def generate_email_fixture():
    return generate_email()

@pytest.fixture
def generate_password_fixture():
    return generate_password()

@pytest.fixture
def registration_data(generate_email_fixture, generate_password_fixture):
    email, name = generate_email_fixture
    password = generate_password_fixture
    return {
        "email": email,
        "name": name,
        "password": password
    }
