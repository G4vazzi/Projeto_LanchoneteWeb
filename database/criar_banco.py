import sqlite3

conexao = sqlite3.connect("database.db")

cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS produtos(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    nome TEXT NOT NULL,

    descricao TEXT NOT NULL,

    preco REAL NOT NULL,

    imagem TEXT

)
""")

conexao.commit()

conexao.close()

print("Banco criado com sucesso!")

cursor.execute("""
CREATE TABLE IF NOT EXISTS administradores(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    usuario TEXT UNIQUE NOT NULL,

    senha TEXT NOT NULL

)
""")