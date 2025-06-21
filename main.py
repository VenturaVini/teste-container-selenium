#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service

def main():
    print("🚀 Executando projeto: teste-container-selenium")
    print("="*50)
    
    # Configurar Firefox
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    service = Service('/usr/local/bin/geckodriver')
    
    try:
        # Teste 1: Google
        driver = webdriver.Firefox(service=service, options=options)
        driver.get('https://www.google.com')
        print(f"✅ Google - Título: {driver.title}")
        driver.quit()
        
        # Teste 2: GitHub
        driver = webdriver.Firefox(service=service, options=options)
        driver.get('https://github.com/VenturaVini/teste-container-selenium')
        print(f"✅ GitHub - Título: {driver.title}")
        driver.quit()
        
        print("🎉 Todos os testes passaram!")
        
    except Exception as e:
        print(f"❌ Erro: {e}")
        return False
    
    return True

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)