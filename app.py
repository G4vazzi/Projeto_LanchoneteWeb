from flask import (Flask, render_template, session, redirect, request)

from database.database import (
    listar_produtos, 
    buscar_produto_por_id, 
    adicionar_produto, 
    atualizar_produto,
    excluir_produto,
    buscar_admin
    )

import os; from werkzeug.utils import (secure_filename)

app = Flask(__name__)
app.secret_key = "Gato Preto"

UPLOAD_FOLDER = "static/uploads"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/")
def inicio():

    produtos = listar_produtos()

    return render_template(
        "index.html",
        produtos=produtos
    )


@app.route("/adicionar/<int:id_produto>")
def adicionar(id_produto):

    if "carrinho" not in session:
        session["carrinho"] = []

    carrinho = session["carrinho"]

    carrinho.append(id_produto)

    session["carrinho"] = carrinho

    print(session["carrinho"])  # Apenas para testar

    return redirect("/")

@app.route("/carrinho")
def carrinho():

    quantidades = {}

    if "carrinho" in session:

        for id_produto in session["carrinho"]:
            if id_produto in quantidades:
                quantidades[id_produto] += 1
            else:
                quantidades[id_produto] = 1

    itens_carrinho = []

    total = 0

    for id_produto, quantidade in quantidades.items():

        produto = buscar_produto_por_id(id_produto)

        subtotal = produto["preco"] * quantidade

        total += subtotal

        itens_carrinho.append({
            "produto": produto,
            "quantidade": quantidade,
            "subtotal": subtotal
        })

    return render_template(
        "carrinho.html",
        itens_carrinho=itens_carrinho,
        total=total
    )

@app.route("/remover/<int:id_produto>")
def remover(id_produto):

    if "carrinho" in session:

        carrinho = session["carrinho"]

        if id_produto in carrinho:

            carrinho.remove(id_produto)

            session["carrinho"] = carrinho

    return redirect("/carrinho")

@app.route("/finalizar")
def finalizar():

    session.pop("carrinho", None)

    return render_template("pedido_realizado.html")

@app.route("/admin")
def admin():

    if "admin" not in session:
        return redirect("/login")

    produtos = listar_produtos()

    return render_template(
        "admin.html",
        produtos=produtos
    )

@app.route("/admin/novo", methods=["GET", "POST"])
def novo_produto():

    if request.method == "POST":

        nome = request.form["nome"]
        descricao = request.form["descricao"]
        preco = float(request.form["preco"])
        imagem = request.files["imagem"]

        _, extensao = os.path.splitext(imagem.filename)
        nome_imagem = secure_filename(nome.lower().replace(" ", "_")) + extensao

        imagem.save(
            os.path.join(
                app.config["UPLOAD_FOLDER"],
                nome_imagem
            )
        )

        adicionar_produto(
            nome,
            descricao,
            preco,
            nome_imagem
        )

        return redirect("/admin")

    return render_template("novo_produto.html")

@app.route("/admin/editar/<int:id_produto>", methods=["GET", "POST"])
def editar_produto(id_produto):

    produto = buscar_produto_por_id(id_produto)

    if request.method == "POST":

        nome = request.form["nome"]
        descricao = request.form["descricao"]
        preco = float(request.form["preco"])

        imagem = request.files["imagem"]

        if imagem.filename != "":

            _, extensao = os.path.splitext(imagem.filename)

            nome_imagem = secure_filename(
                nome.lower().replace(" ", "_")
            ) + extensao

            imagem.save(
                os.path.join(
                    app.config["UPLOAD_FOLDER"],
                    nome_imagem
                )
            )

        else:

            nome_imagem = produto["imagem"]

        atualizar_produto(
            id_produto,
            nome,
            descricao,
            preco,
            nome_imagem
        )

        return redirect("/admin")

    return render_template(
        "editar_produto.html",
        produto=produto
    )

@app.route("/admin/excluir/<int:id_produto>")
def excluir(id_produto):

    excluir_produto(id_produto)

    return redirect("/admin")

@app.route("/login", methods=["GET","POST"])
def login():

    if request.method == "POST":

        usuario = request.form["usuario"]

        senha = request.form["senha"]

        admin = buscar_admin(usuario)

        if admin and admin["senha"] == senha:

            session["admin"] = admin["usuario"]

            return redirect("/admin")

        return render_template(
            "login.html",
            erro="Usuário ou senha inválidos."
        )

    return render_template("login.html")

@app.route("/logout")
def logout():

    session.pop("admin", None)

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)