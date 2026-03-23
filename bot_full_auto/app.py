historico = []

@app.route("/gerar", methods=["POST"])
def gerar():
    produto = get_produto()
    criar_video(produto)

    historico.append(produto)

    return render_template("dashboard.html", historico=historico)