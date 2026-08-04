from flask import (
    Blueprint,
    render_template,
    session,
    redirect,
    request
)

from database.database import (
    listar_produtos,
    buscar_produto_por_id,
    criar_pedido,
    adicionar_item_pedido
)

loja = Blueprint("loja", __name__)

@loja.route("/")
def inicio():

    produtos = listar_produtos()

    return render_template(
        "index.html",
        produtos=produtos
    )