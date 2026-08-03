from flask import Flask, render_template

app = Flask(__name__)

produtos = [
    {
        "nome": "Supremo Prensado",
        "descricao": "Pão, 2 salsichas cortadas ao meio, molho de tomate hand made, milho, tomate picado, batata palha, maionese da casa, chedar cremoso e farofa de bacon.",
        "preco": 44.50,
        "emoji": "🌭",
        "imagem": "Supremo Prensado.jpg"
    },
    {
        "nome": "Cabuloso Prensado",
        "descricao": "Pão, 2 salsichas cortadas ao meio, molho de tomate hand made, vinagrete, batata palha, maionese a casa, molho 4 queijos, alho torrao e tempero verde.",
        "preco": 41.50,
        "emoji": "🌭",
        "imagem": "Cabuloso_Prensado.jpg"
    },
    {
        "nome": "Furioso Prensado",
        "descricao": "Pão, 2 salsichas cortadas ao meio, molho de tomate hand made, vinagrete especial, barbecue, batata palha, lascas de provolone, chedar cremoso, Doritos e farofa de bacon.",
        "preco": 43.50,
        "emoji": "🌭",
        "imagem": "Furioso_Prensado.jpg"
    },
    {
        "nome": "Fantastico Prensado",
        "descricao": "Pao , 2 salsichas na chapa, molho de tomate hand made, vinagrete especial, milho, cheddar cremoso, queijo colonial, bacon em cubos, batata palha, maionese da casa, prensado",
        "preco": 47.50,
        "emoji": "🌭",
        "imagem": "Fantastico_Prensado.jpg"
    }
]

@app.route("/")
def inicio():
    return render_template("index.html", produtos=produtos)

if __name__ == "__main__":
    app.run(debug=True)