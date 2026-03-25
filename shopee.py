import random

def get_produto():
    produtos = [
        {
            "nome": "Smartwatch D20",
            "preco": "R$ 59,90",
            "link": "https://shopee.com/seulink1"
        },
        {
            "nome": "Fone Bluetooth",
            "preco": "R$ 39,90",
            "link": "https://shopee.com/seulink2"
        }
    ]

    return random.choice(produtos)