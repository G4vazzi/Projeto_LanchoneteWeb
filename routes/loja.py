from flask import (
    Blueprint,
    render_template,
    session,
    redirect,
    request,
    url_for
)

from database.database import (
    listar_produtos,
    buscar_produto_por_id,
    criar_pedido,
    adicionar_item_pedido,
    listar_produtos_destaque
)

loja = Blueprint("loja", __name__)


#Rota da pagina inicial
 
@loja.route("/")
def inicio():

    produtos_destaque = listar_produtos_destaque()

    return render_template(
        "home.html",
        produtos=produtos_destaque
    )

#Rota para adicionar itens no carrinho

@loja.route("/adicionar/<int:id_produto>")
def adicionar(id_produto):

    if "carrinho" not in session:
        session["carrinho"] = []

    carrinho = session["carrinho"]

    carrinho.append(id_produto)

    session["carrinho"] = carrinho

    print(session["carrinho"])  # Apenas para testar

    return redirect(url_for("loja.inicio"))

#Rota da pagina carrinho

@loja.route("/carrinho")
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

#Rota para remover itens do carrinho 

@loja.route("/remover/<int:id_produto>")
def remover(id_produto):

    if "carrinho" in session:

        carrinho = session["carrinho"]

        if id_produto in carrinho:

            carrinho.remove(id_produto)

            session["carrinho"] = carrinho

    return redirect("/carrinho")

#Rota da pagina de checkout

@loja.route("/checkout", methods=["GET", "POST"])
def checkout():

    if "carrinho" not in session or len(session["carrinho"]) == 0:
        return redirect(url_for("loja.inicio"))

    quantidades = {}

    for id_produto in session["carrinho"]:

        if id_produto in quantidades:
            quantidades[id_produto] += 1
        else:
            quantidades[id_produto] = 1

    itens = []

    total = 0

    for id_produto, quantidade in quantidades.items():

        produto = buscar_produto_por_id(id_produto)

        subtotal = produto["preco"] * quantidade

        total += subtotal

        itens.append({
            "produto": produto,
            "quantidade": quantidade,
            "subtotal": subtotal
        })

    if request.method == "POST":

        nome = request.form["nome"]
        telefone = request.form["telefone"]
        endereco = request.form["endereco"]
        observacao = request.form["observacao"]

        pedido_id = criar_pedido(
            nome,
            telefone,
            endereco,
            observacao,
            total
        )

        for item in itens:

            adicionar_item_pedido(
                pedido_id,
                item["produto"]["id"],
                item["quantidade"],
                item["produto"]["preco"]
            )

        session.pop("carrinho", None)

        return redirect("/pedido_realizado")

    return render_template(
        "checkout.html",
        itens=itens,
        total=total
    )

#Rota pagina pedido realizado

@loja.route("/pedido_realizado")
def pedido_realizado():

    return render_template(
        "pedido_realizado.html"
    )

from routes.loja import *
