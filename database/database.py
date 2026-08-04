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