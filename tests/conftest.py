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

