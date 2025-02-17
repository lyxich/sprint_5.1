from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import locators

class TestLogin:
    def test_login_with_home_page_button(self, driver):
        driver.find_element(locators.LK_BUTTON).click() # Нашел и кликнул кнопку Личный Кабинет
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((locators.REG_BUTTON))) # Ожидание для загрузки страницы
        driver.find_element(locators.REG_BUTTON).click() # Нашел и кликнул кнопку Зарегистрироваться
        driver.find_element(locators.LOGIN_AKK_BUTTON).click() # Нашел и кликнул кнопку Войти в аккаунт
        driver.find_element(locators.FIELD_EMAIL_PAGE_LOGIN).send_keys("ilyavolkov018@gmail.com") # Нашел поле "Email" и заполнил его
        driver.find_element(locators.FIELD_PASSWORD_PAGE_LOGIN).send_keys("111111") # Нашел поле "Пароль" и заполнил его
        driver.find_element(locators.LOGIN_BUTTON).click() # Нашел кнопку "Войти" и кликнул по ней
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((locators.PLACE_ORDER_BUTTON))) # Ожидание для загрузки страницы
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/' # Проверил, что перешел на главную страницу

    def test_login_with_personal_cabinet_button(self, driver):
        driver.find_element(locators.LK_BUTTON).click() # Нашел и кликнул кнопку Личный кабинет
        driver.find_element(locators.FIELD_EMAIL_PAGE_LOGIN).send_keys("ilyavolkov018@gmail.com") # Нашел поле "Email" и заполнил его
        driver.find_element(locators.FIELD_PASSWORD_PAGE_LOGIN).send_keys("111111") # Нашел поле "Пароль" и заполнил его
        driver.find_element(locators.LOGIN_BUTTON).click() # Нашел кнопку "Войти" и кликнул по ней
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((locators.PLACE_ORDER_BUTTON))) # Ожидание для загрузки страницы
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/' # Проверил, что перешел на главную страницу

    def test_login_with_registration_form_button(self, driver):
        driver.find_element(locators.LOGIN_AKK_BUTTON).click() # Нашел и кликнул кнопку Войти в аккаунт
        driver.find_element(locators.FIELD_EMAIL_PAGE_LOGIN).send_keys("ilyavolkov018@gmail.com") # Нашел поле "Email" и заполнил его
        driver.find_element(locators.FIELD_PASSWORD_PAGE_LOGIN).send_keys("111111") # Нашел поле "Пароль" и заполнил его
        driver.find_element(locators.LOGIN_BUTTON).click() # Нашел кнопку "Войти" и кликнул по ней
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((locators.PLACE_ORDER_BUTTON))) # Ожидание для загрузки страницы
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/' # Проверил, что перешел на главную страницу

    def test_login_with_recovery_password_form_button(self, driver):
        driver.find_element(locators.LK_BUTTON).click() # Нашел и кликнул кнопку Личный Кабинет
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((locators.REG_BUTTON))) # Ожидание для загрузки страницы
        driver.find_element(locators.RECOVER_PASSWORD).click() # Нашел и кликнул кнопку Восстановить пароль
        driver.find_element(locators.LOGIN_BUTTON).click() # Нашел и кликнул кнопку Войти
        driver.find_element(locators.FIELD_EMAIL_PAGE_LOGIN).send_keys("ilyavolkov018@gmail.com") # Нашел поле "Email" и заполнил его
        driver.find_element(locators.FIELD_PASSWORD_PAGE_LOGIN).send_keys("111111") # Нашел поле "Пароль" и заполнил его
        driver.find_element(locators.LOGIN_BUTTON).click() # Нашел кнопку "Войти" и кликнул по ней
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((locators.PLACE_ORDER_BUTTON))) # Ожидание для загрузки страницы
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/' # Проверил, что перешел на главную страницу