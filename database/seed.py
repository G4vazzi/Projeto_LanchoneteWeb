import sqlite3

conexao = sqlite3.connect("database.db")
cursor = conexao.cursor()

produtos = [
    {
        "id": 1,
        "nome": "Supremo Prensado",
        "descricao": "Pão, 2 salsichas cortadas ao meio, molho de tomate hand made, milho, tomate picado, batata palha, maionese da casa, chedar cremoso e farofa de bacon.",
        "preco": 44.50,
        "emoji": "🌭",
        "imagem": "Supremo Prensado.jpg"
    },
    {
        "id": 2,
        "nome": "Cabuloso Prensado",
        "descricao": "Pão, 2 salsichas cortadas ao meio, molho de tomate hand made, vinagrete, batata palha, maionese a casa, molho 4 queijos, alho torrao e tempero verde.",
        "preco": 41.50,
        "emoji": "🌭",
        "imagem": "Cabuloso_Prensado.jpg"
    },
    {
        "id": 3,
        "nome": "Furioso Prensado",
        "descricao": "Pão, 2 salsichas cortadas ao meio, molho de tomate hand made, vinagrete especial, barbecue, batata palha, lascas de provolone, chedar cremoso, Doritos e farofa de bacon.",
        "preco": 43.50,
        "emoji": "🌭",
        "imagem": "Furioso_Prensado.jpg"
    },
    {
        "id": 4,
        "nome": "Fantastico Prensado",
        "descricao": "Pao , 2 salsichas na chapa, molho de tomate hand made, vinagrete especial, milho, cheddar cremoso, queijo colonial, bacon em cubos, batata palha, maionese da casa, prensado",
        "preco": 47.50,
        "emoji": "🌭",
        "imagem": "Fantastico_Prensado.jpg"
    }
]

for produto in produtos:

    cursor.execute("""
    INSERT INTO produtos
    (nome, descricao, preco, imagem)
    VALUES (?, ?, ?, ?)
    """, (
        produto["nome"],
        produto["descricao"],
        produto["preco"],
        produto["imagem"]
    ))

conexao.commit()
conexao.close()

print("Produtos cadastrados com sucesso!")

cursor.execute("""

INSERT INTO administradores

(usuario, senha)

VALUES (?,?)

""", (

"admin",

"123456"

))