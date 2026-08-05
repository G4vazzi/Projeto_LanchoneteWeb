from flask import(
    Blueprint,
    render_template,
    request
)

from database.database import(
    listar_produtos,
    pesquisar_produtos,
    listar_produtos_categoria,
    listar_categorias
)

paginas = Blueprint("paginas", __name__)

@paginas.route("/cardapio")
def cardapio():

    pesquisa = request.args.get("pesquisa", "")
    categoria_selecionada = request.args.get("categoria", "")

    categorias = listar_categorias()

    if pesquisa:

        produtos = pesquisar_produtos(pesquisa)

    elif categoria_selecionada:

        produtos = listar_produtos_categoria(categoria_selecionada)

    else:

        produtos = listar_produtos()

    return render_template(
        "cardapio.html",
        produtos=produtos,
        pesquisa=pesquisa,
        categoria_selecionada=categoria_selecionada,
        categorias=categorias
    )