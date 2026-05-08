from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

def test_google_lucky_button():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    try:
        driver.get("https://www.google.com")
        wait = WebDriverWait(driver, 10)

        # Закрываем куки (если есть)
        try:
            accept_cookies = wait.until(EC.element_to_be_clickable((
                By.XPATH, "//button[contains(., 'Принять') or contains(., 'Accept')]"
            )))
            accept_cookies.click()
        except Exception:
            pass

        # 1. Пробуем найти кнопку 'Мне повезёт' без ввода текста
        lucky_locators = [
            (By.XPATH, "//input[@value='Мне повезёт']"),           # русская версия
            (By.XPATH, "//input[@value=\"I'm Feeling Lucky\"]"),  # английская версия
            (By.NAME, "btnI"),                                   # классический name
            (By.XPATH, "//input[@aria-label='Мне повезёт']"),
            (By.XPATH, "//input[@aria-label=\"I'm Feeling Lucky\"]")
        ]
        lucky_button = None
        for locator in lucky_locators:
            try:
                lucky_button = wait.until(EC.visibility_of_element_located(locator))
                if lucky_button and lucky_button.is_displayed():
                    break
            except:
                continue

        # 2. Если кнопка не найдена – возможно, она появляется только после ввода текста
        if lucky_button is None:
            # Вводим что-нибудь в поле поиска
            search_input = wait.until(EC.visibility_of_element_located((By.NAME, "q")))
            search_input.send_keys("Selenium")
            # Пробуем снова найти кнопку после ввода
            for locator in lucky_locators:
                try:
                    lucky_button = wait.until(EC.visibility_of_element_located(locator))
                    if lucky_button and lucky_button.is_displayed():
                        break
                except:
                    continue

        assert lucky_button is not None, "Кнопка 'Мне повезёт' не найдена на странице"
        assert lucky_button.is_displayed(), "Кнопка не отображается"
    finally:
        driver.quit()