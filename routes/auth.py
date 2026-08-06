from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    session,
    flash,
    url_for
)

from database.database import (
    adicionar_admin,
    buscar_admin_por_email,
    buscar_cliente_por_email,
)

from werkzeug.security import (
    check_password_hash,
    generate_password_hash
)

auth = Blueprint("auth", __name__)

#Rota da pagina de login 

@auth.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        senha = request.form["senha"]

        # -------------------------
        # ADMINISTRADOR
        # -------------------------

        admin = buscar_admin_por_email(email)

        if admin:

            if check_password_hash(admin["senha"], senha):

                session.clear()

                session["admin"] = admin["id"]
                session["nome"] = admin["nome"]

                return redirect(url_for("admin.painel"))

        # -------------------------
        # CLIENTE
        # -------------------------

        cliente = buscar_cliente_por_email(email)

        if cliente:

            if check_password_hash(cliente["senha"], senha):

                session.clear()

                session["cliente"] = cliente["id"]
                session["nome"] = cliente["nome"]

                return redirect(url_for("loja.inicio"))

        return render_template(
            "auth/login.html",
            erro="E-mail ou senha inválidos."
        )

    return render_template("auth/login.html")

#Rota de cadastro de adm 

@auth.route("/cadastrar-admin", methods=["GET", "POST"])
def cadastrar_admin():

    if request.method == "POST":

        nome = request.form["nome"]
        email = request.form["email"]
        senha = request.form["senha"]
        confirmar = request.form["confirmar"]

        # Senhas iguais?
        if senha != confirmar:

            return render_template(
                "auth/cadastrar_admin.html",
                erro="As senhas não coincidem."
            )

        # E-mail já existe?
        admin = buscar_admin_por_email(email)

        if admin:

            return render_template(
                "auth/cadastrar_admin.html",
                erro="Este e-mail já está cadastrado."
            )

        senha_hash = generate_password_hash(senha)

        adicionar_admin(
            nome,
            email,
            senha_hash
        )

        return redirect(url_for("auth.login"))

    return render_template(
        "auth/cadastrar_admin.html"
    )

@auth.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("loja.inicio"))