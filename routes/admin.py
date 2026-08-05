from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    session,
    flash,
    url_for,
    current_app
)

import os

from werkzeug.utils import secure_filename

from database.database import *

admin = Blueprint("admin", __name__)

#Rota para pagina adimin

@admin.route("/admin")
def painel():

    if "admin" not in session:
        return redirect(url_for("auth.login"))

    produtos = listar_produtos()
    dados = dashboard()

    return render_template(
        "admin.html",
        produtos=produtos,
        dashboard=dados
    )

#Rota para adicionar um novo produto

@admin.route("/admin/novo", methods=["GET", "POST"])
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
                current_app.config["UPLOAD_FOLDER"],
                nome_imagem
            )
        )

        adicionar_produto(
            nome,
            descricao,
            preco,
            nome_imagem
        )

        return redirect(url_for("admin.painel"))

    return render_template("novo_produto.html")

#Rota para editar um produto 

@admin.route("/admin/editar/<int:id_produto>", methods=["GET", "POST"])
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
                    current_app.config["UPLOAD_FOLDER"],
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

        return redirect(url_for("admin.painel"))

    return render_template(
        "editar_produto.html",
        produto=produto
    )

#Rota para excluir um produto 

@admin.route("/admin/excluir/<int:id_produto>")
def excluir(id_produto):

    excluir_produto(id_produto)

    return redirect(url_for("admin.painel"))