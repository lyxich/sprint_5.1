from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://stellarburgers.nomoreparties.site/")

# Нашел и кликнул кнопку Войти в аккаунт
driver.find_element(By.XPATH, "//button[contains(@class, 'button_button__33qZ0') and contains(@class, 'button_button_size_large__G21Vg') and text()='Войти в аккаунт']").click()

# Нашел поле "Email" и заполнил его
driver.find_element(By.XPATH, "//div[contains(@class, 'input_type_text') and contains(@class, 'input_size_default')]//input[@type='text' and @name='name']").send_keys("ilyavolkov018@gmail.com")

# Нашел поле "Пароль" и заполнил его
driver.find_element(By.XPATH, "//div[contains(@class, 'input_type_password') and contains(@class, 'input_size_default')]//input[@type='password' and @name='Пароль']").send_keys("111111")

# Нашел кнопку "Войти" и кликнул по ней
driver.find_element(By.XPATH, "//button[contains(@class, 'button_button__33qZ0') and contains(@class, 'button_button_type_primary__1O7Bx') and text()='Войти']").click()

# Ожидание для загрузки страницы
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "//button[contains(@class, 'button_button__33qZ0') and contains(@class, 'button_button_size_large__G21Vg') and text()='Оформить заказ']")))

# Нашел и кликнул вкладку Соусы
driver.find_element(By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG') and contains(., 'Соусы')]").click()

# Проверил, что вкладка Соусы стала активной

assert "tab_tab_type_current" in driver.find_element(By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG') and contains(., 'Соусы')]").get_attribute('class')

# Нашел и кликнул вкладку Начинки
driver.find_element(By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG') and contains(., 'Начинки')]").click()

# Проверил, что вкладка Начинки стала активной

assert "tab_tab_type_current" in driver.find_element(By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG') and contains(., 'Начинки')]").get_attribute('class')

# Нашел и кликнул вкладку Булки
driver.find_element(By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG') and contains(., 'Булки')]").click()

# Проверил, что вкладка Булки стала активной

assert "tab_tab_type_current" in driver.find_element(By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG') and contains(., 'Булки')]").get_attribute('class')

driver.quit()