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


if __name__ == "__main__":
    app.run(debug=True)