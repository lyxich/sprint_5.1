from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import locators

class TestRegistration:
    def test_correct_registration(self, driver):
        driver.find_element(locators.LK_BUTTON).click() # Нашел и кликнул кнопку Личный Кабинет
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((locators.REG_BUTTON))) # Ожидание для загрузки страницы
        driver.find_element(locators.REG_BUTTON).click() # Нашел и кликнул кнопку Зарегистрироваться
        driver.find_element(locators.FIELD_NAME).send_keys("1") # Нашел поле "Имя" и заполнил его
        driver.find_element(locators.FIELD_EMAIL).send_keys("ilyavolkov018@gmail.com")# Нашел поле "Email" и заполнил его
        driver.find_element(locators.FIELD_PASSWORD).send_keys("111111") # Нашел поле "Пароль" и заполнил его некорректным значением
        driver.find_element(locators.REG_BUTTON_FOR_REG) and text() = 'Зарегистрироваться']").click() # Нашел кнопку "Зарегистрироваться" и кликнул по ней
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((locators.LOGIN_BUTTON))) # Ожидание для загрузки страницы
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login' # Проверил, что перешел на страницу входа

    def test_incorrect_registration(self, driver):
        driver.find_element(locators.LK_BUTTON).click() # Нашел и кликнул кнопку Личный Кабинет
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((locators.REG_BUTTON))) # Ожидание для загрузки страницы
        driver.find_element(locators.REG_BUTTON).click() # Нашел и кликнул кнопку Зарегистрироваться
        driver.find_element(locators.FIELD_NAME).send_keys("1") # Нашел поле "Имя" и заполнил его
        driver.find_element(locators.FIELD_EMAIL).send_keys("ilyavolkov018@gmail.com") # Нашел поле "Email" и заполнил его
        driver.find_element(locators.FIELD_PASSWORD).send_keys("1") # Нашел поле "Пароль" и заполнил его некорректным значением
        driver.find_element(locators.REG_BUTTON_FOR_REG).click() # Нашел кнопку "Зарегистрироваться" и кликнул по ней
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((locators.INCORRECT_PASS))) # Дождался надписи Некорректный пароль
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/register' # Проверил, что остался на странице регистрации