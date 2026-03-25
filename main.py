from shopee import get_produto
from video import criar_video
from post_instagram import postar

produto = get_produto()

print("Produto:", produto)

criar_video(produto)

postar()