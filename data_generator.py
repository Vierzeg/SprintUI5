# tests/helpers.py
import random
import string
from transliterate import translit


# Список русских имен
names = [
    "Александр", "Дмитрий", "Павел", "Роман", "Николай",
    "Виктория", "Оля", "Элеонора", "Марина", "Алиса"
]

user_data = {
    "email": "pavel44prac@ya.ru",
    "password": "DF45hgg_35"
}

def generate_email():
    #Генерация случайного email.
    random_name = random.choice(names)
    transliterated_name = translit(random_name, 'ru', reversed=True).lower()
    random_string = ''.join(random.choices(string.digits, k=4))
    email = f"{transliterated_name}{random_string}@yandex.ru"
    return email, random_name

def generate_password():
    #Генерация случайного пароля.
    length = random.randint(6, 12)
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    return password
