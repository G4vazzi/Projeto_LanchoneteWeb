from flask import(
    Blueprint,
    render_template,
    session,
    redirect,
    url_for
)

from database.database import *

pedidos = Blueprint("pedidos", __name__)

#Rota para listar os pedidos 

@pedidos.route("/pedidos")
def listar_pedidos():

    if "admin" not in session:
        return redirect(url_for("auth.login"))

    pedidos_lista = listar_todos_pedidos()

    return render_template(
        "pedidos.html",
        pedidos=pedidos_lista
    )

#Rota para visualizar os pedidos 

@pedidos.route("/pedido/<int:id_pedido>")
def visualizar_pedido(id_pedido):

    if "admin" not in session:
        return redirect(url_for("auth.login"))

    pedido = buscar_pedido_por_id(id_pedido)

    itens = listar_itens_pedido(id_pedido)

    return render_template(
        "pedido.html",
        pedido=pedido,
        itens=itens
    )

@pedidos.route("/pedido/status/<int:id_pedido>/<status>")
def alterar_status(id_pedido, status):

    if "admin" not in session:
        return redirect(url_for("auth.login"))

    alterar_status_pedido(id_pedido, status)

    return redirect(url_for("pedidos.visualizar_pedido", id_pedido=id_pedido))