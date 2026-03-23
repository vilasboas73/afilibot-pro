from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def responder():
    driver = webdriver.Chrome()
    driver.get("https://www.instagram.com/")

    print("👉 Faça login manual...")
    time.sleep(60)

    print("👉 Abra o post com comentários...")
    input("Pressione ENTER quando estiver pronto...")

    comentarios = driver.find_elements(By.XPATH, "//span")

    for comentario in comentarios:
        texto = comentario.text.lower()

        if "link" in texto:
            try:
                comentario.click()
                time.sleep(2)

                campo = driver.find_element(By.TAG_NAME, "textarea")
                campo.send_keys("🔥 Aqui está o link do produto: https://seulink.com")

                print("✅ Respondido")

            except:
                print("Erro ao responder")

    time.sleep(10)
    driver.quit()