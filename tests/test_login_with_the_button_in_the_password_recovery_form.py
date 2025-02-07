from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")

# Нашел и кликнул кнопку Личный Кабинет
driver.find_element(By.XPATH, ".//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']").click()

# Ожидание для загрузки страницы
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "Auth_link__1fOlj")))

# Нашел и кликнул кнопку Восстановить пароль
driver.find_element(By.XPATH, "//a[@class='Auth_link__1fOlj' and @href='/forgot-password' and text()='Восстановить пароль']").click()

# Нашел и кликнул кнопку Войти
driver.find_element(By.XPATH, "//a[@class='Auth_link__1fOlj' and @href='/login' and text()='Войти']").click()

# Нашел поле "Email" и заполнил его
driver.find_element(By.XPATH, "//div[contains(@class, 'input_type_text') and contains(@class, 'input_size_default')]//input[@type='text' and @name='name']").send_keys("ilyavolkov018@gmail.com")

# Нашел поле "Пароль" и заполнил его
driver.find_element(By.XPATH, "//div[contains(@class, 'input_type_password') and contains(@class, 'input_size_default')]//input[@type='password' and @name='Пароль']").send_keys("111111")

# Нашел кнопку "Войти" и кликнул по ней
driver.find_element(By.XPATH, "//button[contains(@class, 'button_button__33qZ0') and contains(@class, 'button_button_type_primary__1O7Bx') and text()='Войти']").click()

# Ожидание для загрузки страницы
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//button[contains(@class, 'button_button__33qZ0') and contains(@class, 'button_button_size_large__G21Vg') and text()='Оформить заказ']")))

# Проверил, что перешел на главную страницу
assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

driver.quit()