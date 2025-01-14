import pandas as pd

# recebe dados
def recebe_dados():
    nome =  str(input("Nome da planta: "))
    preco =  str(input("Preço: "))
    preferencia =  str(input("Preferência: "))

    # velida preço
    if preco.isnumeric():
        preco = float(preco)

    produto = [nome, preco, preferencia]
    return produto
