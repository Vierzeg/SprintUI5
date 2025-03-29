# tests/locators.py

from selenium.webdriver.common.by import By


# Локаторы для регистрации и входа
REGISTER_NAME_FIELD = (By.XPATH, "//input[@name='name']")# Поле для имени
REGISTER_EMAIL_FIELD = (By.XPATH, "//input[@value='']")# Поле для email
REGISTER_PASSWORD_FIELD = (By.XPATH, "//input[@name='Пароль']")# Поле для пароля
REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']") # Кнопка регистрации

ODER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']") # Кнопка "Оформить заказ"
LOGO_BUTTON = (By.XPATH, ".//div[@class='AppHeader_header__logo__2D0X2']") # Кнопка Лототип
LOGIN_BUTTON_MAIN = (By.XPATH, "//button[text()='Войти в аккаунт']") # Кнопка на главной странице
LOGIN_EMAIL_FIELD = (By.XPATH, "//input[@value='']")# Поле для ввода email на странице входа
LOGIN_PASSWORD_FIELD = (By.XPATH, "//input[@name='Пароль']")# Поле для ввода пароля
LOGIN_SUBMIT_BUTTON = (By.XPATH, "//button[text()='Войти']")  # Кнопка для входа
LOGIN_FROM_REG_BUTTON = (By.XPATH, "//a[text()='Войти']")# Кнопка войти в форме регистрации
REC_PASS_BUTTON = (By.XPATH, "//a[text()='Восстановить пароль']")# Кнопка восстановить пароль
LOGIN_REC_PASS_BUTTON = (By.XPATH, "//a[text()='Войти']")# Кнопка войти на странице восстановления пароля

# Локаторы для личного кабинета и переходов
PROFILE_BUTTON = (By.XPATH, "//a[p[text()='Личный Кабинет']]")  # Кнопка личного кабинета
LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")  # Кнопка выхода
# Локаторы для конструктора
CONSTRUCTOR_BUTTON = (By.LINK_TEXT, "Конструктор")
CONSTRUCTOR_BUNS_BUTTON = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG') and .//span[text()='Булки']]")# Кнопка "Булки"
CONSTRUCTOR_SAUCES_BUTTON = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG') and .//span[text()='Соусы']]")# Кнопка "Соусы"
CONSTRUCTOR_FILLINGS_BUTTON = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG') and .//span[text()='Начинки']]")# Кнопка "Начинки"
