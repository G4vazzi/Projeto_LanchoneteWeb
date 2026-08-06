from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    session,
    flash
)

from database.database import (
    buscar_admin,
    cadastrar_admin
)

auth = Blueprint("auth", __name__)

#Rota da pagina de login 

@auth.route("/login", methods=["GET","POST"])
def login():

    if request.method == "POST":

        usuario = request.form["usuario"]

        senha = request.form["senha"]

        admin = buscar_admin(usuario)

        if admin:

            if admin["senha"] == senha:

                session["admin"] = admin["nome"]

                return redirect("/admin")

        return render_template(
            "auth/login.html",
            erro="Usuário ou senha inválidos."
        )

    return render_template("auth/login.html")

#Rota da pagina de logout

@auth.route("/logout")
def logout():

    session.pop("admin", None)

    flash("Logout realizado com sucesso! ")

    return redirect("/")

#Rota da cadastrar_adm

@auth.route("/admin/cadastrar", methods=["GET", "POST"])
def cadastrar_administrador():

    if request.method == "POST":

        nome = request.form["nome"]

        usuario = request.form["usuario"]

        senha = request.form["senha"]

        cadastrar_admin(
            nome,
            usuario,
            senha
        )

        return redirect("/login")

    return render_template("auth/cadastrar_admin.html")