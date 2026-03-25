from flask import Flask, render_template, request, redirect, session
import os
import json

app = Flask(__name__)
app.secret_key = "segredo123"

# =========================
# BANCO (JSON)
# =========================
def carregar_usuarios():
    try:
        with open("users.json", "r") as f:
            return json.load(f)
    except:
        return []

def salvar_usuarios(usuarios):
    with open("users.json", "w") as f:
        json.dump(usuarios, f, indent=4)

# =========================
# HOME (PROTEGIDA)
# =========================
@app.route("/")
def home():
    if "user" not in session:
        return redirect("/login")
    return render_template("index.html")

# =========================
# CADASTRO
# =========================
@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":
        user = request.form["user"]
        pwd = request.form["pwd"]

        usuarios = carregar_usuarios()

        for u in usuarios:
            if u["user"] == user:
                return "Usuário já existe"

        novo = {
            "user": user,
            "pwd": pwd,
            "ativo": False,
            "cliques": 0,
            "ganhos": 0
        }

        usuarios.append(novo)
        salvar_usuarios(usuarios)

        return redirect("/login")

    return render_template("cadastro.html")

# =========================
# LOGIN
# =========================
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = request.form["user"]
        pwd = request.form["pwd"]

        usuarios = carregar_usuarios()

        for u in usuarios:
            if u["user"] == user and u["pwd"] == pwd:

                if not u["ativo"]:
                    return redirect("/bloqueado")

                session["user"] = user
                return redirect("/")

        return "Login inválido"

    return render_template("login.html")

# =========================
# BLOQUEADO
# =========================
@app.route("/bloqueado")
def bloqueado():
    return """
    <h1>🔒 Acesso bloqueado</h1>
    <p>Você precisa comprar para liberar</p>
    <a href="/vendas">👉 Comprar acesso</a>
    """

# =========================
# DASHBOARD
# =========================
@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect("/login")

    usuarios = carregar_usuarios()

    for u in usuarios:
        if u["user"] == session["user"]:
            return render_template("dashboard.html", user=u)

    return "Usuário não encontrado"

# =========================
# LIBERAR USUÁRIO
# =========================
@app.route("/liberar/<user>")
def liberar(user):
    usuarios = carregar_usuarios()

    for u in usuarios:
        if u["user"] == user:
            u["ativo"] = True

    salvar_usuarios(usuarios)

    return f"{user} liberado com sucesso!"

# =========================
# LOGOUT (CORRIGIDO)
# =========================
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")

# =========================
# VENDAS
# =========================
@app.route("/vendas")
def vendas():
    return render_template("vendas.html")

# =========================
# RENDER (OBRIGATÓRIO)
# =========================
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)