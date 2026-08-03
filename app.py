from flask import Flask, render_template, session, redirect
from database.database import listar_produtos, buscar_produto_por_id

app = Flask(__name__)
app.secret_key = "Gato Preto"


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

    produtos_carrinho = []

    total = 0

    if "carrinho" in session:

        for id_produto in session["carrinho"]:

            produto = buscar_produto_por_id(id_produto)

            if produto:

                produtos_carrinho.append(produto)

                total += produto["preco"]

    return render_template(
        "carrinho.html",
        produtos=produtos_carrinho,
        total=total
    )


if __name__ == "__main__":
    app.run(debug=True)