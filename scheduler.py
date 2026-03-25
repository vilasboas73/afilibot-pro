import time
from shopee import get_produto
from video import criar_video
from telegram_bot import enviar_oferta

while True:
    produto = get_produto()

    criar_video(produto)
    enviar_oferta()

    time.sleep(3600)