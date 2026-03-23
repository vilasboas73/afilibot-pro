from flask import Flask, render_template, request, redirect
from video import criar_video
from shopee import get_produto
import os

app = Flask(__name__)

# histórico simples (memória)
historico = []

@app.route("/")
def home():
    try:
        return render_template("index.html")
    except Exception as e:
        return f"Erro ao carregar HTML: {e}"

@app.route("/gerar", methods=["POST"])
def gerar():
    try:
        produto = get_produto()
        criar_video(produto)

        historico.append(produto)

        return render_template("dashboard.html", historico=historico)

    except Exception as e:
        return f"Erro ao gerar vídeo: {e}"

# LOGIN SIMPLES
usuario = "admin"
senha = "123"

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = request.form["user"]
        pwd = request.form["pwd"]

        if user == usuario and pwd == senha:
            return redirect("/")
        else:
            return "Login inválido"

    return render_template("login.html")


# RODAR ONLINE (Render)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)