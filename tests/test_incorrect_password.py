from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")

# Нашел и кликнул кнопку Личный Кабинет
driver.find_element(By.XPATH, ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']").click()
#driver.find_element(By.CLASS_NAME, "AppHeader_header__link__3D_hX").click()

WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "Auth_link__1fOlj")))

# Нашел и кликнул кнопку Зарегистрироваться
driver.find_element(By.CLASS_NAME, "Auth_link__1fOlj").click()

# Нашел поле "Имя" и заполнил его
driver.find_element(By.XPATH, "//input[@type='text' and @name='name']").send_keys("1")

# Нашел поле "Email" и заполнил его
driver.find_element(By.XPATH, "//input[@type='text' and @name='name' and @value='']").send_keys("ilyavolkov018@gmail.com")

# Нашел поле "Пароль" и заполнил его некорректным значением
driver.find_element(By.XPATH, "//input[@type='password' and @name='Пароль']").send_keys("1")

# Нашел кнопку "Зарегистрироваться" и кликнул по ней
driver.find_element(By.XPATH, "//button[contains(@class, 'button_button__33qZ0') and text()='Зарегистрироваться']").click()

# Дождался надписи Некорректный пароль
WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, "//p[@class='input__error text_type_main-default' and text()='Некорректный пароль']")))

# Проверил, что остался на странице регистрации
assert driver.current_url == 'https://stellarburgers.nomoreparties.site/register'

driver.quit()