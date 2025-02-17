from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import locators

class TestClicking:
    def test_clicking_on_constructor(self, driver):
        driver.find_element(locators.LK_BUTTON).click() # Нашел и кликнул кнопку Войти в аккаунт
        driver.find_element(locators.FIELD_EMAIL_PAGE_LOGIN).send_keys("ilyavolkov018@gmail.com")  # Нашел поле "Email" и заполнил его
        driver.find_element(locators.FIELD_PASSWORD_PAGE_LOGIN).send_keys("111111") # Нашел поле "Пароль" и заполнил его
        driver.find_element(locators.LOGIN_BUTTON).click() # Нашел кнопку "Войти" и кликнул по ней
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((locators.PLACE_ORDER_BUTTON))) # Ожидание для загрузки страницы
        driver.find_element(locators.LK_BUTTON).click() # Нашел и кликнул кнопку Личный кабинет
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((locators.LOGOUT_BUTTON))) # Ожидание для загрузки страницы
        driver.find_element(locators.CONSTRUCTOR_BUTTON).click() # Нашел и кликнул кнопку Конструктор
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((locators.PLACE_ORDER_BUTTON))) # Ожидание для загрузки страницы
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/' # Проверил, что перешел на главную страницу

    def test_clicking_on_logo(self, driver):
        driver.find_element(locators.LOGIN_AKK_BUTTON).click() # Нашел и кликнул кнопку Войти в аккаунт
        driver.find_element(locators.FIELD_EMAIL_PAGE_LOGIN).send_keys("ilyavolkov018@gmail.com") # Нашел поле "Email" и заполнил его
        driver.find_element(locators.FIELD_PASSWORD_PAGE_LOGIN).send_keys("111111") # Нашел поле "Пароль" и заполнил его
        driver.find_element(locators.LOGIN_BUTTON).click() # Нашел кнопку "Войти" и кликнул по ней
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((locators.PLACE_ORDER_BUTTON))) # Ожидание для загрузки страницы
        driver.find_element(locators.LK_BUTTON).click() # Нашел и кликнул кнопку Личный кабинет
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((locators.LOGOUT_BUTTON))) # Ожидание для загрузки страницы
        driver.find_element(locators.LOGO).click() # Нашел и кликнул на логотип
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((locators.PLACE_ORDER_BUTTON))) # Ожидание для загрузки страницы
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/' # Проверил, что перешел на главную страницу

    def test_clicking_on_my_account(self, driver):
        driver.find_element(locators.LOGIN_AKK_BUTTON).click() # Нашел и кликнул кнопку Войти в аккаунт
        driver.find_element(locators.FIELD_EMAIL_PAGE_LOGIN).send_keys("ilyavolkov018@gmail.com") # Нашел поле "Email" и заполнил его
        driver.find_element(locators.FIELD_PASSWORD_PAGE_LOGIN).send_keys("111111") # Нашел поле "Пароль" и заполнил его
        driver.find_element(locators.LOGIN_BUTTON).click() # Нашел кнопку "Войти" и кликнул по ней
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((locators.PLACE_ORDER_BUTTON))) # Ожидание для загрузки страницы
        driver.find_element(locators.LK_BUTTON).click() # Нашел и кликнул кнопку Личный кабинет
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((locators.LOGOUT_BUTTON))) # Ожидание для загрузки страницы
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile' # Проверил, что перешел на страницу личного кабинета