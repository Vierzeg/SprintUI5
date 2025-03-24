# tests/test_constructor.py
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *

def test_sauces_section(driver):
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/main/section[1]/div[1]/div[2]"))
    ).click()
    time.sleep(1)
    sauces_section = driver.find_element(By.XPATH, "//*[contains(@class, 'tab_tab_type_current')]")

    # Проверка, что элемент найден с нужным классом
    assert sauces_section, "Элемент с классом 'tab_tab_type_current' не найден"

def test_buns_section(driver):
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/main/section[1]/div[1]/div[1]"))
    ).click()
    time.sleep(1)
    buns_button = driver.find_element(By.XPATH, "//*[contains(@class, 'tab_tab_type_current')]")

    # Проверка, что элемент найден с нужным классом
    assert buns_button, "Элемент с классом 'tab_tab_type_current' не найден"

def test_fillings_section(driver):
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/main/section[1]/div[1]/div[3]"))
    ).click()
    time.sleep(1)
    fillings_section = driver.find_element(By.XPATH, "//*[contains(@class, 'tab_tab_type_current')]")

    # Проверка, что элемент найден с нужным классом
    assert fillings_section, "Элемент с классом 'tab_tab_type_current' не найден"


