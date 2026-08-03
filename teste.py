from flask import session


quantidades = {}

for id_produto in session["carrinho"]:
    if id_produto in quantidades:
        quantidades[id_produto] += 1
    else:
        quantidades[id_produto] = 1