import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium_client import SeleniumClient
from services.telegram import enviar_mensagem

def main():
    base_url = 'https://www.youtube.com'
    url = f'{base_url}/watch?v=zuYWJ2AVvPw'
    client = SeleniumClient()
    driver = client.iniciar_driver(url)

    if not driver:
        print("❌ Falha ao iniciar navegador.")
        return

    wait = WebDriverWait(driver, 15)

    try:
        for i in range(10):
            print(f"\n🔄 Iteração {i+1}: Acessando {url}")
            driver.get(url)

            # Espera o vídeo carregar totalmente
            wait.until(EC.visibility_of_element_located((
                By.XPATH,
                '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-watch-metadata/div/div[2]/div[1]/ytd-video-owner-renderer/a/yt-img-shadow/img'
            )))

            title = driver.title
            print(f"🎬 Título: {title}")

            # Enviar mensagem via Telegram
            try:
                if title.strip():
                    enviar_mensagem(f"📺 Vídeo: {title}")
                    print("📩 Enviado no Telegram.")
                else:
                    print("⚠️ Título vazio, não enviado ao Telegram.")
            except Exception as e:
                print(f"⚠️ Erro ao enviar para o Telegram: {e}")

            # Espera e coleta o próximo link
            try:
                sugestoes = driver.find_elements(By.CLASS_NAME, 'yt-simple-endpoint')
                links_validos = [el.get_attribute('href') for el in sugestoes if el.get_attribute('href')]
                proximos_youtube = [link for link in links_validos if '/watch?' in link]

                if not proximos_youtube:
                    print("❌ Nenhum próximo vídeo válido encontrado.")
                    break

                url = proximos_youtube[-1]  # Pega o primeiro
                # print(proximos_youtube)
                time.sleep(5)
                print(f"➡️ Próximo vídeo: {url}")
            except Exception as e:
                print(f"⚠️ Erro ao encontrar próximo vídeo: {e}")
                break

            time.sleep(2)

    except Exception as e:
        print(f"💥 Erro durante execução: {e}")
    finally:
        driver.quit()
        print("🧹 Navegador fechado.")

if __name__ == "__main__":
    main()
