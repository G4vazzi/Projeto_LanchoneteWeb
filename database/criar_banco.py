import sqlite3

conexao = sqlite3.connect("database.db")

cursor = conexao.cursor()

# Tabela de produtos
cursor.execute("""
CREATE TABLE IF NOT EXISTS produtos(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    nome TEXT NOT NULL,

    descricao TEXT NOT NULL,

    preco REAL NOT NULL,

    imagem TEXT

)
""")

# Tabela de administradores
cursor.execute("""
CREATE TABLE IF NOT EXISTS administradores(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    usuario TEXT UNIQUE NOT NULL,

    senha TEXT NOT NULL,

    nome TEXT NOT NULL

)
""")

conexao.commit()

conexao.close()

print("Banco criado com sucesso!")