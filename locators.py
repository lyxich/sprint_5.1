from selenium.webdriver.common.by import By

class Locators:

    LK_BUTTON = (By.XPATH, ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']") # Кнопка Личный Кабинет

    REG_BUTTON = (By.CLASS_NAME, "Auth_link__1fOlj") # Кнопка Зарегистрироваться

    FIELD_NAME = (By.XPATH, "//input[@type='text' and @name='name']") # Поле "Имя" на странице регистрации

    FIELD_EMAIL = (By.XPATH, "//input[@type='text' and @name='name' and @value='']") # Поле "Email" на странице регистрации

    FIELD_PASSWORD = (By.XPATH, "//input[@type='password' and @name='Пароль']") # Поле "Пароль" на странице регистрации

    REG_BUTTON_FOR_REG = (By.XPATH, "//button[contains(@class, 'button_button__33qZ0') and text()='Зарегистрироваться']") # Кнопка Зарегистрироваться

    LOGIN_AKK_BUTTON = (By.XPATH, "//button[contains(@class, 'button_button__33qZ0') and contains(@class, 'button_button_size_large__G21Vg') and text()='Войти в аккаунт']") # Кнопка Войти в аккаунт

    FIELD_EMAIL_PAGE_LOGIN = (By.XPATH, "//div[contains(@class, 'input_type_text') and contains(@class, 'input_size_default')]//input[@type='text' and @name='name']") # Поле "Email" на странице входа

    FIELD_PASSWORD_PAGE_LOGIN = (By.XPATH, "//div[contains(@class, 'input_type_password') and contains(@class, 'input_size_default')]//input[@type='password' and @name='Пароль']") # Поле "Пароль" на странице входа

    LOGIN_BUTTON = (By.XPATH, "//button[contains(@class, 'button_button__33qZ0') and contains(@class, 'button_button_type_primary__1O7Bx') and text()='Войти']") # Кнопка "Войти"

    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[@class='AppHeader_header__linkText__3q_va ml-2' and text()='Конструктор']") # Кнопка Конструктор

    LOGO = (By.CSS_SELECTOR, "div.AppHeader_header__logo__2D0X2 a[href='/']") # Логотип

    LOGOUT_BUTTON = (By.XPATH, "//li[@class='Account_listItem__35dAP']//button[contains(@class, 'Account_button__14Yp3') and text()='Выход']") # Кнопка Выход

    SOUSES = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG') and contains(., 'Соусы')]") # Вкладка Соусы

    TOPPINGS = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG') and contains(., 'Начинки')]") # Вкладка Начинки

    BUNS = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG') and contains(., 'Булки')]") # Вкладка Булки

    PLACE_ORDER_BUTTON = (By.XPATH, "//button[contains(@class, 'button_button__33qZ0') and contains(@class, 'button_button_size_large__G21Vg') and text()='Оформить заказ']") # Кнопка Оформить заказ

    INCORRECT_PASS = (By.XPATH, "//p[@class='input__error text_type_main-default' and text()='Некорректный пароль']")

    RECOVER_PASSWORD = (By.XPATH, "//a[@class='Auth_link__1fOlj' and @href='/forgot-password' and text()='Восстановить пароль']")