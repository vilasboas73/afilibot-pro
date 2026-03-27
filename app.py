from flask import Flask, render_template, request, redirect, session
import os, json

app = Flask(__name__)
app.secret_key = "segredo123"

# banco seguro
def carregar_usuarios():
    if not os.path.exists("users.json"):
        with open("users.json", "w") as f:
            f.write("[]")
    try:
        with open("users.json", "r") as f:
            return json.load(f)
    except:
        return []

def salvar_usuarios(data):
    with open("users.json", "w") as f:
        json.dump(data, f, indent=4)

@app.route("/")
def home():
    if "user" not in session:
        return redirect("/login")
    return render_template("index.html")

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        user = request.form.get("user")
        pwd = request.form.get("pwd")

        for u in carregar_usuarios():
            if u["user"] == user and u["pwd"] == pwd:
                if not u["ativo"]:
                    return redirect("/bloqueado")
                session["user"] = user
                return redirect("/")
        return "Login inválido"

    return render_template("login.html")

@app.route("/cadastro", methods=["GET","POST"])
def cadastro():
    if request.method == "POST":
        user = request.form.get("user")
        pwd = request.form.get("pwd")

        data = carregar_usuarios()

        data.append({
            "user": user,
            "pwd": pwd,
            "ativo": False,
            "ganhos": 0
        })

        salvar_usuarios(data)
        return redirect("/login")

    return render_template("cadastro.html")

@app.route("/bloqueado")
def bloqueado():
    return "<h1>🔒 Compre para liberar</h1><a href='/vendas'>Comprar</a>"

@app.route("/vendas")
def vendas():
    return render_template("vendas.html")

@app.route("/liberar/<user>")
def liberar(user):
    data = carregar_usuarios()
    for u in data:
        if u["user"] == user:
            u["ativo"] = True
    salvar_usuarios(data)
    return "Liberado"

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")