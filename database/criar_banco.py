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

# Tabela de pedidos
cursor.execute("""
CREATE TABLE IF NOT EXISTS pedidos(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    cliente TEXT NOT NULL,

    telefone TEXT NOT NULL,

    endereco TEXT NOT NULL,

    observacao TEXT,

    total REAL NOT NULL,

    status TEXT DEFAULT 'Recebido'

)
""")

# Produtos do pedido
cursor.execute("""
CREATE TABLE IF NOT EXISTS itens_pedido(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    pedido_id INTEGER NOT NULL,

    produto_id INTEGER NOT NULL,

    quantidade INTEGER NOT NULL,

    preco REAL NOT NULL,

    FOREIGN KEY(pedido_id) REFERENCES pedidos(id),

    FOREIGN KEY(produto_id) REFERENCES produtos(id)

)
""")

conexao.commit()

conexao.close()

print("Banco criado com sucesso!")