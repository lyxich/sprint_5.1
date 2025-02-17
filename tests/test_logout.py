from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestLogout:
    def test_logout(self, driver):
        driver.find_element(locators.LOGIN_AKK_BUTTON).click() # Нашел и кликнул кнопку Войти в аккаунт
        driver.find_element(locators.FIELD_EMAIL_PAGE_LOGIN).send_keys("ilyavolkov018@gmail.com") # Нашел поле "Email" и заполнил его
        driver.find_element(locators.FIELD_PASSWORD_PAGE_LOGIN).send_keys("111111") # Нашел поле "Пароль" и заполнил его
        driver.find_element(locators.LOGIN_BUTTON).click() # Нашел кнопку "Войти" и кликнул по ней
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((locators.PLACE_ORDER_BUTTON))) # Ожидание для загрузки страницы
        driver.find_element(locators.LK_BUTTON).click() # Нашел и кликнул кнопку Личный кабинет
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((locators.LOGOUT_BUTTON))) # Ожидание для загрузки страницы
        driver.find_element(locators.LOGOUT_BUTTON).click() # Нашел и кликнул кнопку Выход
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((locators.LOGIN_BUTTON)))# Ожидание для загрузки страницы
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login' # Проверил, что перешел на страницу входа