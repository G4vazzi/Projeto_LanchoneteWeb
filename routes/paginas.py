from flask import(
    Blueprint,
    render_template 
)

paginas = Blueprint("paginas", __name__)

@paginas.route("/cardapio")
def cardapio():

    return render_template("cardapio.html")