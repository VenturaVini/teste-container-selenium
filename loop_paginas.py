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

    wait = WebDriverWait(driver, 15)  # timeout 15 segundos para espera explícita

    try:
        for i in range(10):
            print(f"🔄 Iteração {i+1}: Acessando {url}")
            driver.get(url)

            # Espera o elemento específico estar visível antes de continuar
            wait.until(EC.visibility_of_element_located((
                By.XPATH,
                '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-watch-metadata/div/div[2]/div[1]/ytd-video-owner-renderer/a/yt-img-shadow/img'
            )))

            title = driver.title
            print(f"Título: {title}")

            # Envia título pro Telegram
            enviar_mensagem(f"Título do vídeo: {title}")
            print("Mensagem enviada no Telegram!")

            # Pega href do próximo vídeo
            try:
                next_video_element = driver.find_element(
                    By.XPATH,
                    '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[2]/div/div[4]/ytd-watch-next-secondary-results-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-compact-video-renderer[1]/div[1]/div/div[1]/a'
                )
                href = next_video_element.get_attribute('href')
                if not href:
                    print("⚠️ Próximo vídeo sem href válido. Encerrando loop.")
                    break
                url = href
            except Exception as e:
                print(f"⚠️ Erro ao pegar próximo vídeo: {e}")
                break

            time.sleep(5)  # espera 2 seg antes da próxima iteração

    except Exception as e:
        print(f"⚠️ Erro durante scraping: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
