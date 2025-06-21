#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
import sys

def configurar_firefox():
    """Configura o Firefox para ambiente containerizado"""
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')
    options.add_argument('--window-size=1920,1080')
    
    # Service com o caminho do geckodriver
    service = Service('/usr/local/bin/geckodriver')
    
    return options, service

def testar_site(url, nome_site):
    """Testa um site específico"""
    options, service = configurar_firefox()
    driver = None
    
    try:
        print(f"🌐 Testando {nome_site}...")
        driver = webdriver.Firefox(service=service, options=options)
        driver.set_page_load_timeout(30)
        driver.get(url)
        
        titulo = driver.title
        print(f"✅ {nome_site} - Título: {titulo}")
        return True
        
    except Exception as e:
        print(f"❌ Erro ao testar {nome_site}: {str(e)}")
        return False
    
    finally:
        if driver:
            try:
                driver.quit()
            except Exception as e:
                print(f"⚠️ Erro ao fechar driver: {str(e)}")

def main():
    print("🚀 Executando projeto: teste-container-selenium")
    print("="*50)
    
    testes_passou = 0
    total_testes = 0
    
    # Lista de testes
    testes = [
        ('https://www.google.com', 'Google'),
        ('https://github.com/VenturaVini/teste-container-selenium', 'GitHub'),
        ('https://www.wikipedia.org', 'Wikipedia')
    ]
    
    # Executar testes
    for url, nome in testes:
        total_testes += 1
        if testar_site(url, nome):
            testes_passou += 1
        
        # Pequena pausa entre testes
        import time
        time.sleep(1)
    
    # Resultado final
    print("\n" + "="*50)
    print(f"📊 Resultado: {testes_passou}/{total_testes} testes passaram")
    
    if testes_passou == total_testes:
        print("🎉 Todos os testes passaram!")
        return True
    else:
        print(f"⚠️ {total_testes - testes_passou} teste(s) falharam!")
        return False

if __name__ == "__main__":
    try:
        success = main()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n🛑 Execução interrompida pelo usuário")
        sys.exit(1)
    except Exception as e:
        print(f"💥 Erro crítico não tratado: {str(e)}")
        sys.exit(1)