from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash
)

from werkzeug.security import generate_password_hash

from database.database import (
    cadastrar_cliente,
    buscar_cliente_por_email
)

clientes = Blueprint("clientes", __name__)

@clientes.route("/cadastro", methods=["GET", "POST"])
def cadastro():

    if request.method == "POST":

        nome = request.form["nome"]
        email = request.form["email"]
        telefone = request.form["telefone"]
        endereco = request.form["endereco"]
        senha = request.form["senha"]
        confirmar = request.form["confirmar"]

        # Verifica se as senhas são iguais
        if senha != confirmar:

            flash("As senhas não coincidem.")

            return redirect(url_for("clientes.cadastro"))

        # Verifica se o e-mail já existe
        cliente = buscar_cliente_por_email(email)

        if cliente:

            flash("Este e-mail já está cadastrado.")

            return redirect(url_for("clientes.cadastro"))

        # Criptografa a senha
        senha_hash = generate_password_hash(senha)

        # Salva no banco
        cadastrar_cliente(
            nome,
            email,
            telefone,
            senha_hash,
            endereco
        )

        flash("Conta criada com sucesso!")

        return redirect(url_for("clientes.login"))

    return render_template(
        "clientes/cadastro.html"
    )