from flask import Flask, render_template, request, redirect, session
import os
import json

app = Flask(__name__)
app.secret_key = "segredo123"

# =========================
# BANCO (SEGURO)
# =========================
def carregar_usuarios():
    if not os.path.exists("users.json"):
        with open("users.json", "w") as f:
            f.write("[]")

    with open("users.json", "r") as f:
        return json.load(f)

def salvar_usuarios(usuarios):
    with open("users.json", "w") as f:
        json.dump(usuarios, f, indent=4)

# =========================
# ROTAS
# =========================
@app.route("/")
def home():
    if "user" not in session:
        return redirect("/login")
    return render_template("index.html")

@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":
        user = request.form.get("user")
        pwd = request.form.get("pwd")

        usuarios = carregar_usuarios()

        for u in usuarios:
            if u["user"] == user:
                return "Usuário já existe"

        usuarios.append({
            "user": user,
            "pwd": pwd,
            "ativo": False,
            "cliques": 0,
            "ganhos": 0
        })

        salvar_usuarios(usuarios)
        return redirect("/login")

    return render_template("cadastro.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = request.form.get("user")
        pwd = request.form.get("pwd")

        usuarios = carregar_usuarios()

        for u in usuarios:
            if u["user"] == user and u["pwd"] == pwd:

                if not u["ativo"]:
                    return redirect("/bloqueado")

                session["user"] = user
                return redirect("/")

        return "Login inválido"

    return render_template("login.html")

@app.route("/bloqueado")
def bloqueado():
    return "<h1>🔒 Compre para liberar</h1><a href='/vendas'>Comprar</a>"

@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect("/login")

    usuarios = carregar_usuarios()

    for u in usuarios:
        if u["user"] == session["user"]:
            return render_template("dashboard.html", user=u)

@app.route("/liberar/<user>")
def liberar(user):
    usuarios = carregar_usuarios()

    for u in usuarios:
        if u["user"] == user:
            u["ativo"] = True

    salvar_usuarios(usuarios)
    return "Liberado!"

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")

@app.route("/vendas")
def vendas():
    return render_template("vendas.html")