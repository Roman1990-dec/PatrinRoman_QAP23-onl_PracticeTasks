from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

class GoogleMainPage:
    # Локатор элементов (с поддержкой разных языков)
    SEARCH_INPUT = (By.NAME, "q")

    # Кнопка "Поиск в Google" / "Google Search" (несколько вариантов для разных языков)
    GOOGLE_SEARCH_BUTTON = (
        By.XPATH, 
        "//input[@value='Поиск в Google' or @value='Google Search' or @name='btnK']"
    )

    # Кнопка "Мне повезёт" / "I'm Feeling Lucky"
    LUCKY_BUTTON = (
        By.XPATH, 
        "//input[@value='Мне повезёт' or @value=\"I'm Feeling Lucky\" or @name='btnI']"
    )

    # URL главной страницы Google
    BASE_URL = "https://www.google.com"

    def __init__(self, driver):
        """
        Инициализация страницы с драйвером.
        
        Args:
            driver: WebDriver экземпляр
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def open(self):
        """
        Переход на главную страницу Google.
        """
        self.driver.get(self.BASE_URL)
    
    def enter_search_query(self, query: str):
        """
        Ввод значения в поле поиска.
        
        Args:
            query: Строка для поиска
        """
        search_input = self.wait.until(EC.visibility_of_element_located(self.SEARCH_INPUT))
        search_input.clear()
        search_input.send_keys(query)
    
    def click_google_search(self):
        """
        Клик по кнопке 'Google search' / 'Поиск в Google'.
        """
        search_button = self.wait.until(EC.element_to_be_clickable(self.GOOGLE_SEARCH_BUTTON))
        search_button.click()
    
    def click_lucky_button(self):
        """
        Клик по кнопке 'I'm feeling lucky' / 'Мне повезёт'.
        """
        lucky_button = self.wait.until(EC.element_to_be_clickable(self.LUCKY_BUTTON))
        lucky_button.click()
    
    def input_yahoo_search(self):
        """
        Ввод значения 'yahoo search' в поле поиска
        """
        self.enter_search_query("yahoo search")
    
    def is_current_page_google_main(self) -> bool:
        """
        Проверка, что текущая страница является главной страницей Google.
        
        Returns:
            bool: True если текущая страница - главная Google, иначе False
        """
        current_url = self.driver.current_url
        # Проверяем URL и наличие поля поиска на странице
        if "google.com" not in current_url:
            return False
        
        try:
            # Проверяем, что поле поиска присутствует на странице
            self.wait.until(EC.visibility_of_element_located(self.SEARCH_INPUT))
            return True
        except Exception:
            return False

def test_google_main_page():
    """
    Тест для проверки методов класса GoogleMainPage.
    """
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    
    try:
        # Создаём объект страницы
        google_page = GoogleMainPage(driver)
        
        # Открываем главную страницу Google
        google_page.open()
        
        # Проверяем, что мы на главной странице
        assert google_page.is_current_page_google_main()
        
        # Вводим 'yahoo search'
        google_page.input_yahoo_search()
                
        # Кликаем по кнопке 'I'm feeling lucky' / 'Мне повезёт'
        google_page.click_lucky_button()      
    finally:
        driver.quit()