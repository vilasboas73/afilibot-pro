from flask import Flask, render_template, request, redirect
import os

# IMPORTA SUAS FUNÇÕES (se não existir ainda, não quebra)
try:
    from video import criar_video
except:
    criar_video = None

try:
    from shopee import get_produto
except:
    get_produto = None

app = Flask(__name__)

# histórico simples
historico = []

# =========================
# HOME
# =========================
@app.route("/")
def home():
    try:
        return render_template("index.html")
    except Exception as e:
        return f"Erro na HOME: {e}"

# =========================
# GERAR VÍDEO
# =========================
@app.route("/gerar", methods=["POST"])
def gerar():
    try:
        if not get_produto or not criar_video:
            return "⚠️ Função de vídeo ainda não configurada"

        produto = get_produto()
        criar_video(produto)

        historico.append(produto)

        return render_template("dashboard.html", historico=historico)

    except Exception as e:
        return f"Erro ao gerar vídeo: {e}"

# =========================
# LOGIN SIMPLES
# =========================
usuario = "admin"
senha = "123"

@app.route("/login", methods=["GET", "POST"])
def login():
    try:
        if request.method == "POST":
            user = request.form.get("user")
            pwd = request.form.get("pwd")

            if user == usuario and pwd == senha:
                return redirect("/")
            else:
                return "Login inválido"

        return render_template("login.html")

    except Exception as e:
        return f"Erro no login: {e}"

# =========================
# DASHBOARD
# =========================
@app.route("/dashboard")
def dashboard():
    try:
        return render_template("dashboard.html", historico=historico)
    except Exception as e:
        return f"Erro no dashboard: {e}"

# =========================
# PÁGINA DE VENDAS
# =========================
@app.route("/vendas")
def vendas():
    try:
        return render_template("vendas.html")
    except Exception as e:
        return f"Erro na página de vendas: {e}"

# =========================
# RENDER (OBRIGATÓRIO)
# =========================
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)