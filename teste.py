from selenium_client import SeleniumClient
from services.telegram import enviar_mensagem

def main():
    url = 'https://www.youtube.com/watch?v=zuYWJ2AVvPw'
    client = SeleniumClient()
    driver = client.iniciar_driver(url)

    if not driver:
        print("❌ Falha ao iniciar navegador.")
        return

    try:
        # 👇 Aqui você faz seu scraping como quiser
        print(f"Título: {driver.title}")
        h1 = driver.find_element("tag name", "h1")
        print(f"Texto Extraido: {h1.text}")
        enviar_mensagem(h1.text)
    except Exception as e:
        print(f"⚠️ Erro durante scraping: {str(e)}")
    finally:
        driver.quit()


main()