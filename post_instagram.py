from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def postar():
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get("https://www.instagram.com/")
    
    print("👉 Faça login manual no Instagram...")
    time.sleep(60)

    print("👉 Clique no botão '+'")
    print("👉 Clique em 'Selecionar do computador'")
    print("👉 Escolha o vídeo MANUALMENTE")
    print("👉 Avance até a tela de legenda")
    
    input("👉 Quando estiver na tela de legenda, pressione ENTER aqui...")

    # LEGENDA AUTOMÁTICA
    try:
        campos = driver.find_elements(By.XPATH, "//textarea | //div[@contenteditable='true']")

        if campos:
            campos[0].click()
            campos[0].send_keys("🔥 Produto viral! Comenta LINK 👇")
            print("✅ Legenda adicionada")
        else:
            print("❌ Não encontrou campo de legenda")

    except Exception as e:
        print("Erro legenda:", e)

    time.sleep(3)

    # POSTAR AUTOMÁTICO
    try:
        botoes = driver.find_elements(By.XPATH, "//div[contains(text(),'Compartilhar') or contains(text(),'Share')]")

        if botoes:
            botoes[0].click()
            print("🚀 Postando...")
        else:
            print("❌ Não encontrou botão postar")

    except Exception as e:
        print("Erro postar:", e)

    time.sleep(10)
    print("✅ Finalizado")
    driver.quit()