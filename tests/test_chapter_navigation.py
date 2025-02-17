from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import locators

class TestChapterNavigation:
    def test_open_souses(self, driver):
        driver.find_element(locators.LK_BUTTON).click() # Нашел и кликнул кнопку Войти в аккаунт
        driver.find_element(locators.FIELD_EMAIL_PAGE_LOGIN).send_keys("ilyavolkov018@gmail.com") # Нашел поле "Email" и заполнил его
        driver.find_element(locators.FIELD_PASSWORD_PAGE_LOGIN).send_keys("111111") # Нашел поле "Пароль" и заполнил его
        driver.find_element(locators.LOGIN_BUTTON).click( )# Нашел кнопку "Войти" и кликнул по ней
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((locators.PLACE_ORDER_BUTTON))) # Ожидание для загрузки страницы
        driver.find_element(locators.SOUSES).click() # Нашел и кликнул вкладку Соусы
        assert "tab_tab_type_current" in driver.find_element(locators.SOUSES).get_attribute('class') # Проверил, что вкладка Соусы стала активной

    def test_open_toppings(self, driver):
        driver.find_element(locators.LK_BUTTON).click()  # Нашел и кликнул кнопку Войти в аккаунт
        driver.find_element(locators.FIELD_EMAIL_PAGE_LOGIN).send_keys("ilyavolkov018@gmail.com")  # Нашел поле "Email" и заполнил его
        driver.find_element(locators.FIELD_PASSWORD_PAGE_LOGIN).send_keys("111111")  # Нашел поле "Пароль" и заполнил его
        driver.find_element(locators.LOGIN_BUTTON).click()  # Нашел кнопку "Войти" и кликнул по ней
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((locators.PLACE_ORDER_BUTTON)))  # Ожидание для загрузки страницы
        driver.find_element(locators.TOPPINGS).click() # Нашел и кликнул вкладку Начинки
        assert "tab_tab_type_current" in driver.find_element(locators.TOPPINGS).get_attribute('class') # Проверил, что вкладка Начинки стала активной

    def test_open_buns(self, driver):
        driver.find_element(locators.LK_BUTTON).click()  # Нашел и кликнул кнопку Войти в аккаунт
        driver.find_element(locators.FIELD_EMAIL_PAGE_LOGIN).send_keys("ilyavolkov018@gmail.com")  # Нашел поле "Email" и заполнил его
        driver.find_element(locators.FIELD_PASSWORD_PAGE_LOGIN).send_keys("111111")  # Нашел поле "Пароль" и заполнил его
        driver.find_element(locators.LOGIN_BUTTON).click()  # Нашел кнопку "Войти" и кликнул по ней
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((locators.PLACE_ORDER_BUTTON)))  # Ожидание для загрузки страницы
        driver.find_element(locators.SOUSES).click()  # Нашел и кликнул вкладку Соусы
        assert "tab_tab_type_current" in driver.find_element(locators.SOUSES).get_attribute('class')  # Проверил, что вкладка Соусы стала активной
        driver.find_element(locators.BUNS).click() # Нашел и кликнул вкладку Булки
        assert "tab_tab_type_current" in driver.find_element(locators.BUNS).get_attribute('class') # Проверил, что вкладка Булки стала активной