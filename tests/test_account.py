# tests/test_account.py

import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *
from data_generator import user_data


class TestProfileAccess:

    def test_profile_access(self, driver_acc):  # Проверка кнопки перехода в личный кабинет
        WebDriverWait(driver_acc, 10).until(EC.presence_of_element_located(PROFILE_BUTTON)).click()

        # Проверяем, что страница личного кабинета загрузилась
        WebDriverWait(driver_acc, 10).until(EC.presence_of_element_located(PROFILE_BUTTON))

        # Assert: Проверяем, что заголовок личного кабинета отображается на странице
        assert driver_acc.find_element(*PROFILE_BUTTON).is_displayed(), "Не удалось перейти в Личный Кабинет!"

    def test_const_from_profile(self, driver_log):  # Проверка перехода в конструктор из личного кабинета
        # Используем данные из модуля user_data для входа
        email = user_data["email"]
        password = user_data["password"]

        WebDriverWait(driver_log, 10).until(EC.presence_of_element_located(LOGIN_EMAIL_FIELD)).send_keys(
            email)  # Вводм Email
        WebDriverWait(driver_log, 10).until(EC.presence_of_element_located(LOGIN_PASSWORD_FIELD)).send_keys(
            password)  # Вводим Пароль
        WebDriverWait(driver_log, 10).until(EC.presence_of_element_located(LOGIN_SUBMIT_BUTTON)).click()
        WebDriverWait(driver_log, 10).until(EC.presence_of_element_located(PROFILE_BUTTON)).click()
        constructor_button = WebDriverWait(driver_log, 10).until(EC.presence_of_element_located(CONSTRUCTOR_BUTTON))
        constructor_button.click()

        # Проверка, что кнопка "Конструктор" доступна
        assert constructor_button.is_displayed(), "Конструктор не отображается на странице"

    def test_logo_from_profile(self, driver_log):  # Проверка перехода в конструктор из личного кабинета
        # Используем данные из модуля user_data для входа
        email = user_data["email"]
        password = user_data["password"]

        WebDriverWait(driver_log, 10).until(EC.presence_of_element_located(LOGIN_EMAIL_FIELD)).send_keys(
            email)  # Вводм Email
        WebDriverWait(driver_log, 10).until(EC.presence_of_element_located(LOGIN_PASSWORD_FIELD)).send_keys(
            password)  # Вводим Пароль
        WebDriverWait(driver_log, 10).until(EC.presence_of_element_located(LOGIN_SUBMIT_BUTTON)).click()
        WebDriverWait(driver_log, 10).until(EC.presence_of_element_located(PROFILE_BUTTON)).click()
        WebDriverWait(driver_log, 10).until(EC.presence_of_element_located(LOGOUT_BUTTON)).click()

        logo_butt_acc = WebDriverWait(driver_log, 10).until(
            EC.presence_of_element_located(LOGO_BUTTON)
        )
        # Проверка, что класс логотипа соответствует ожидаемому
        assert "AppHeader_header__logo__2D0X2" in logo_butt_acc.get_attribute("class")


class TestLogin:

    def test_login_from_main_button(self, driver_acc):  # Проверка входа в ЛК с главной страницы
        # Используем данные из модуля user_data для входа
        email = user_data["email"]
        password = user_data["password"]

        WebDriverWait(driver_acc, 10).until(EC.presence_of_element_located(
            LOGIN_BUTTON_MAIN)).click()  # Кликаем на кнопу "Войти в аккаунт" на главной странице
        WebDriverWait(driver_acc, 10).until(EC.presence_of_element_located(LOGIN_EMAIL_FIELD)).send_keys(
            email)  # Вводим Email
        WebDriverWait(driver_acc, 10).until(EC.presence_of_element_located(LOGIN_PASSWORD_FIELD)).send_keys(
            password)  # Вводим Пароль
        WebDriverWait(driver_acc, 10).until(
            EC.presence_of_element_located(LOGIN_SUBMIT_BUTTON)).click()  # Кликаем на кнопу "Войти"

       #Проверяем, что кнопка "Оформить заказ" появилась и доступна для клика
        order_button = WebDriverWait(driver_acc, 10).until(
            EC.element_to_be_clickable(ODER_BUTTON)
        )

        # Assert: проверка, что кнопка "Оформить заказ" кликабельна
        assert order_button.is_displayed(), "Кнопка 'Оформить заказ' не отображается после входа"
        assert order_button.is_enabled(), "Кнопка 'Оформить заказ' недоступна для клика после входа"

    def test_login_profile_access(self, driver_acc):  # Проверка авторизации через кнопку "Личного кабинета"
        # Используем данные из модуля user_data для входа
        email = user_data["email"]
        password = user_data["password"]

        WebDriverWait(driver_acc, 10).until(EC.presence_of_element_located(
            PROFILE_BUTTON)).click()  # Кликаем на кнопу "Личный кабинет" на главной странице
        WebDriverWait(driver_acc, 10).until(EC.presence_of_element_located(LOGIN_EMAIL_FIELD)).send_keys(
            email)  # Вводим Email
        WebDriverWait(driver_acc, 10).until(EC.presence_of_element_located(LOGIN_PASSWORD_FIELD)).send_keys(
            password)  # Вводим Пароль
        WebDriverWait(driver_acc, 10).until(
            EC.presence_of_element_located(LOGIN_SUBMIT_BUTTON)).click()  # Кликаем на кнопу "Войти"

        # Проверяем, что кнопка "Оформить заказ" появилась и доступна для клика
        order_button = WebDriverWait(driver_acc, 10).until(
            EC.element_to_be_clickable(ODER_BUTTON)
        )

        # Assert: проверка, что кнопка "Оформить заказ" кликабельна
        assert order_button.is_displayed(), "Кнопка 'Оформить заказ' не отображается после входа"
        assert order_button.is_enabled(), "Кнопка 'Оформить заказ' недоступна для клика после входа"

    def test_login_reg_form(self, driver_reg):  # Проверка авторизации через окно регистрации
        # Используем данные из модуля user_data для входа
        email = user_data["email"]
        password = user_data["password"]

        WebDriverWait(driver_reg, 10).until(EC.presence_of_element_located(
            LOGIN_FROM_REG_BUTTON)).click()  # Кликаем на кнопу "Личный кабинет" на главной странице
        WebDriverWait(driver_reg, 10).until(EC.presence_of_element_located(LOGIN_EMAIL_FIELD)).send_keys(
            email)  # Вводим Email
        WebDriverWait(driver_reg, 10).until(EC.presence_of_element_located(LOGIN_PASSWORD_FIELD)).send_keys(
            password)  # Вводим Пароль
        WebDriverWait(driver_reg, 10).until(
            EC.presence_of_element_located(LOGIN_SUBMIT_BUTTON)).click()  # Кликаем на кнопу "Войти"

        # Проверяем, что кнопка "Оформить заказ" появилась и доступна для клика
        order_button = WebDriverWait(driver_reg, 10).until(
            EC.element_to_be_clickable(ODER_BUTTON)
        )

        # Assert: проверка, что кнопка "Оформить заказ" кликабельна
        assert order_button.is_displayed(), "Кнопка 'Оформить заказ' не отображается после входа"
        assert order_button.is_enabled(), "Кнопка 'Оформить заказ' недоступна для клика после входа"

    def test_login_rec_pass(self, driver_log):  # Проверка входа в аккаунт через окно "восстановления пароля"
        # Используем данные из модуля user_data для входа
        email = user_data["email"]
        password = user_data["password"]

        WebDriverWait(driver_log, 10).until(EC.presence_of_element_located(
            REC_PASS_BUTTON)).click()  # Кликаем на кнопу "Восстановить пароль" на странице авторизации
        WebDriverWait(driver_log, 10).until(EC.presence_of_element_located(LOGIN_REC_PASS_BUTTON)).click()
        WebDriverWait(driver_log, 10).until(EC.presence_of_element_located(LOGIN_EMAIL_FIELD)).send_keys(
            email)  # Вводим Email
        WebDriverWait(driver_log, 10).until(EC.presence_of_element_located(LOGIN_PASSWORD_FIELD)).send_keys(
            password)  # Вводим Пароль
        WebDriverWait(driver_log, 10).until(
            EC.presence_of_element_located(LOGIN_SUBMIT_BUTTON)).click()  # Кликаем на кнопу "Войти"

        # Проверяем, что кнопка "Оформить заказ" появилась и доступна для клика
        order_button = WebDriverWait(driver_log, 10).until(
            EC.element_to_be_clickable(ODER_BUTTON)
        )

        # Assert: проверка, что кнопка "Оформить заказ" кликабельна
        assert order_button.is_displayed(), "Кнопка 'Оформить заказ' не отображается после входа"
        assert order_button.is_enabled(), "Кнопка 'Оформить заказ' недоступна для клика после входа"

    def test_out_from_profile(self, driver_log):  # Проверяем кнопку выхода из профиля
        # Используем данные из модуля user_data для входа
        email = user_data["email"]
        password = user_data["password"]

        WebDriverWait(driver_log, 10).until(EC.presence_of_element_located(LOGIN_EMAIL_FIELD)).send_keys(
            email)  # Вводим Email
        WebDriverWait(driver_log, 10).until(EC.presence_of_element_located(LOGIN_PASSWORD_FIELD)).send_keys(
            password)  # Вводим Пароль
        WebDriverWait(driver_log, 10).until(EC.presence_of_element_located(LOGIN_SUBMIT_BUTTON)).click()
        WebDriverWait(driver_log, 10).until(EC.presence_of_element_located(PROFILE_BUTTON)).click()
        WebDriverWait(driver_log, 10).until(EC.presence_of_element_located(LOGOUT_BUTTON)).click()

        # Проверяем, что поля для ввода Email и Пароля стали видимыми и активными (не пустыми)
        email_field = WebDriverWait(driver_log, 10).until(EC.presence_of_element_located(LOGIN_EMAIL_FIELD))
        password_field = WebDriverWait(driver_log, 10).until(EC.presence_of_element_located(LOGIN_PASSWORD_FIELD))

        # Assert: Проверяем, что поля для ввода Email и Пароля активны и видимы
        assert email_field.is_displayed(), "Поле для ввода email не отображается!"
        assert password_field.is_displayed(), "Поле для ввода пароля не отображается!"

        # Assert: Проверяем, что поля пустые и готовы для ввода
        assert email_field.get_attribute("value") == "", "Поле для ввода email не пустое!"
        assert password_field.get_attribute("value") == "", "Поле для ввода пароля не пустое!"

        # Дополнительная проверка: можно проверить, что поля активны для ввода
        assert email_field.is_enabled(), "Поле для ввода email не активно!"
        assert password_field.is_enabled(), "Поле для ввода пароля не активно!"