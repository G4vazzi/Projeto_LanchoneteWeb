import sqlite3


def conectar():
    conexao = sqlite3.connect("database.db")
    conexao.row_factory = sqlite3.Row
    return conexao

    

def listar_produtos():

    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute("""
        SELECT
            id,
            nome,
            descricao,
            preco,
            imagem
        FROM produtos
    """)

    produtos = cursor.fetchall()

    conexao.close()

    return produtos



def buscar_produto_por_id(id_produto):

    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute("""
        SELECT
            id,
            nome,
            descricao,
            preco,
            imagem
        FROM produtos
        WHERE id = ?
    """, (id_produto,))

    produto = cursor.fetchone()

    conexao.close()

    return produto

def adicionar_produto(nome, descricao, preco, imagem):

    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO produtos
        (nome, descricao, preco, imagem)
        VALUES (?, ?, ?, ?)
    """, (nome, descricao, preco, imagem))

    conexao.commit()

    conexao.close()

def atualizar_produto(id, nome, descricao, preco, imagem):

    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute("""
        UPDATE produtos
        SET
            nome = ?,
            descricao = ?,
            preco = ?,
            imagem = ?
        WHERE id = ?
    """, (
        nome,
        descricao,
        preco,
        imagem,
        id
    ))

    conexao.commit()

    conexao.close()

def excluir_produto(id_produto):

    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute("""
        DELETE FROM produtos
        WHERE id = ?
    """, (id_produto,))

    conexao.commit()

    conexao.close()

def buscar_admin(usuario):

    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute("""

    SELECT *

    FROM administradores

    WHERE usuario = ?

    """, (usuario,))

    admin = cursor.fetchone()

    conexao.close()

    return admin

def cadastrar_admin(nome, usuario, senha):

    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute("""

        INSERT INTO administradores
        (nome, usuario, senha)

        VALUES (?, ?, ?)

    """, (

        nome,
        usuario,
        senha

    ))

    conexao.commit()

    conexao.close()

def criar_pedido(cliente, telefone, endereco, observacao, total):

    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO pedidos
        (cliente, telefone, endereco, observacao, total)

        VALUES (?, ?, ?, ?, ?)
    """, (
        cliente,
        telefone,
        endereco,
        observacao,
        total
    ))

    conexao.commit()

    pedido_id = cursor.lastrowid

    conexao.close()

    return pedido_id

def adicionar_item_pedido(
    pedido_id,
    produto_id,
    quantidade,
    preco
):

    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO itens_pedido
        (
            pedido_id,
            produto_id,
            quantidade,
            preco
        )

        VALUES (?, ?, ?, ?)

    """, (
        pedido_id,
        produto_id,
        quantidade,
        preco
    ))

    conexao.commit()

    conexao.close()

def listar_todos_pedidos():

    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute("""
        SELECT
            id,
            cliente
            telefone,
            total,
            status
        FROM pedidos
        ORDER BY id DESC
    """)

    pedidos = cursor.fetchall()

    conexao.close()

    return pedidos

def buscar_pedido_por_id(id_pedido):

    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute("""
        SELECT
            id,
            cliente,
            telefone,
            endereco,
            observacao,
            total,
            status
        FROM pedidos
        WHERE id = ?
    """,(id_pedido,))

    pedido = cursor.fetchone()

    conexao.close()

    return pedido

def listar_itens_pedido(id_pedido):

    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute("""
        SELECT

            produtos.nome,
            produtos.imagem,

            itens_pedido.quantidade,
            itens_pedido.preco

        FROM itens_pedido

        INNER JOIN produtos

            ON produtos.id = itens_pedido.produto_id

        WHERE pedido_id = ?

    """, (id_pedido,))

    itens = cursor.fetchall()

    conexao.close()

    return itens

def alterar_status_pedido(id_pedido, status):

    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute("""
        UPDATE pedidos
        SET status = ?
        WHERE id = ?
    """, (status, id_pedido))

    conexao.commit()

    conexao.close()

def dashboard():

    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute("SELECT COUNT(*) FROM pedidos")
    total_pedidos = cursor.fetchone()[0]

    cursor.execute("SELECT SUM(total) FROM pedidos")
    faturamento = cursor.fetchone()[0] or 0

    cursor.execute("SELECT COUNT(*) FROM produtos")
    total_produtos = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(DISTINCT telefone) FROM pedidos")
    total_clientes = cursor.fetchone()[0]

    conexao.close()

    return {
        "pedidos": total_pedidos,
        "faturamento": faturamento,
        "produtos": total_produtos,
        "clientes": total_clientes
    }

def pesquisar_produtos(nome):

    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute("""
        SELECT
            id,
            nome,
            descricao,
            preco,
            imagem
        FROM produtos
        WHERE nome LIKE ?
        ORDER BY nome
    """, (f"%{nome}%",))

    produtos = cursor.fetchall()

    conexao.close()

    return produtos