import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def driver():
    driver_service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=driver_service)
    driver.get('https://petfriends.skillfactory.ru/login')
    driver.maximize_window()
    yield driver
    driver.quit()


def test_my_pets_explicit(driver):
    ### Проверка явного ожидания###
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'email')))
    ### Ввод логина ###
    driver.find_element(By.ID, 'email').send_keys('ibobkov91@mail.ru')
    ### Ввод пароля ###
    driver.find_element(By.ID, 'pass').send_keys('Konzra55')
    ### Нажатие кнопки ввода ###
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    ### Проверка, что находимся на главной странице пользователя ###
    assert driver.find_element(By.TAG_NAME, 'h1').text == 'PetFriends'


def test_my_pets_implicit(driver):
    ### Проверка неявного ожидания ###
    driver.find_element(By.ID, 'email').send_keys('ibobkov91@mai.ru')
    driver.find_element(By.ID, 'pass').send_keys('Konzra55')
    driver.implicitly_wait(10)
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    assert driver.find_element(By.TAG_NAME, 'h1').text == 'PetFriends'
