import requests
from shopee import get_produto

TOKEN = "SEU_TOKEN_AQUI"
CHAT_ID = "SEU_CHAT_ID"

def enviar_oferta():
    produto = get_produto()

    mensagem = f"""
🔥 OFERTA DO DIA

📦 {produto['nome']}
💰 {produto['preco']}

👉 {produto['link']}
"""

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    requests.post(url, data={
        "chat_id": CHAT_ID,
        "text": mensagem
    })

    print("✅ Enviado no Telegram")

if __name__ == "__main__":
    enviar_oferta()