from flask import (
    Blueprint,
    render_template
)

clientes = Blueprint("clientes", __name__)

@clientes.route("/cadastro")
def cadastro():

    return render_template(
        "clientes/cadastro.html"
    )