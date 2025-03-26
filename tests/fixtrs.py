# tests/fixtrs.py

import pytest
from selenium import webdriver
from data_generator import *


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
