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