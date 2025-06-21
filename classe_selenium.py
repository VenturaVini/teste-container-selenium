from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service

class SeleniumClient:
    def __init__(self, driver_path='/usr/local/bin/geckodriver', headless=True):
        self.driver_path = driver_path
        self.headless = headless

    def configurar_firefox(self):
        options = Options()
        if self.headless:
            options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-gpu')
        options.add_argument('--window-size=1920,1080')
        service = Service(self.driver_path)
        return options, service

    def iniciar_driver(self, url):
        """Inicializa o driver com a URL carregada e retorna o driver"""
        options, service = self.configurar_firefox()
        driver = None

        try:
            driver = webdriver.Firefox(service=service, options=options)
            driver.set_page_load_timeout(30)
            driver.get(url)
            print(f"✅ Página carregada: {driver.title}")
            return driver
        except Exception as e:
            print(f"❌ Erro ao iniciar driver: {str(e)}")
            if driver:
                try:
                    driver.quit()
                except:
                    pass
            return None
