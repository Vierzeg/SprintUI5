# tests/test_registration.py

import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *


def test_successful_registration(driver_reg, registration_data):
    # Используем данные из фикстуры registration_data
    email = registration_data["email"]
    name = registration_data["name"]
    password = registration_data["password"]

    # Явное ожидание полей и их заполнение
    WebDriverWait(driver_reg, 10).until(EC.presence_of_element_located(REGISTER_NAME_FIELD)).send_keys(name)  # Имя на русском
    WebDriverWait(driver_reg, 10).until(EC.presence_of_element_located(REGISTER_EMAIL_FIELD)).send_keys(email)  # Email на латинице
    WebDriverWait(driver_reg, 10).until(EC.presence_of_element_located(REGISTER_PASSWORD_FIELD)).send_keys(password)

    # Явное ожидание кнопки и её клик
    WebDriverWait(driver_reg, 10).until(EC.element_to_be_clickable(REGISTER_BUTTON)).click()

def test_incor_pass_registration(driver_reg, registration_data):
    # Используем данные из фикстуры registration_data
    email = registration_data["email"]
    name = registration_data["name"]
    password = "wron"  # Неправильный пароль

    # Явное ожидание полей и их заполнение
    WebDriverWait(driver_reg, 10).until(EC.presence_of_element_located(REGISTER_NAME_FIELD)).send_keys(name)  # Имя на русском
    WebDriverWait(driver_reg, 10).until(EC.presence_of_element_located(REGISTER_EMAIL_FIELD)).send_keys(email)  # Email на латинице
    WebDriverWait(driver_reg, 10).until(EC.presence_of_element_located(REGISTER_PASSWORD_FIELD)).send_keys(password)

    # Явное ожидание кнопки и её клик
    WebDriverWait(driver_reg, 10).until(EC.element_to_be_clickable(REGISTER_BUTTON)).click()

    # Явное ожидание появления сообщения об ошибке
    error_message_element = WebDriverWait(driver_reg, 10).until(
        EC.presence_of_element_located((By.XPATH, "//p[contains(text(),'Некорректный пароль')]"))
    )
    error_message = error_message_element.text
    assert "Некорректный пароль" in error_message