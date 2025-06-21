from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service

def main():
    print("🚀 Executando meu projeto Selenium!")
    
    # Configurar Firefox
    options = Options()
    options.add_argument('--headless')
    service = Service('/usr/local/bin/geckodriver')
    
    # Seus testes aqui
    driver = webdriver.Firefox(service=service, options=options)
    
    try:
        # Exemplo: testar seu site
        driver.get('https://www.seusite.com')
        print(f"✅ Título: {driver.title}")
        
        # Adicione mais testes aqui...
        
    except Exception as e:
        print(f"❌ Erro: {e}")
    finally:
        driver.quit()
    
    print("✅ Projeto executado com sucesso!")

if __name__ == "__main__":
    main()