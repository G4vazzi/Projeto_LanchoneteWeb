from flask import (
    Flask, 
    render_template, 
    session, 
    redirect, 
    request,
    flash
    )

from routes.loja import loja
from routes.auth import auth
from routes.admin import admin
from routes.pedidos import pedidos

from database.database import (
    listar_produtos, 
    buscar_produto_por_id, 
    adicionar_produto, 
    atualizar_produto,
    excluir_produto,
    buscar_admin,
    cadastrar_admin,
    criar_pedido,
    adicionar_item_pedido
    )

import os; from werkzeug.utils import (secure_filename)

app = Flask(__name__)

app.register_blueprint(loja)
app.register_blueprint(auth)
app.register_blueprint(admin)
app.register_blueprint(pedidos)

app.secret_key = "Gato Preto"

UPLOAD_FOLDER = "static/uploads"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


if __name__ == "__main__":
    app.run(debug=True) 