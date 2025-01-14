import pandas as pd

# recebe dados
def recebe_dados():
    nome =  str(input("Nome da planta: "))

    # verifica se nome esta preenchido
    while len(nome) <= 2:
        print('Tamanho inválido!')
        nome =  str(input("Nome da planta: "))

    preco =  str(input("Preço: "))

    # verifica se preco esta preenchido
    while len(preco) <= 0:
        print('Preço inválido!')
        preco =  str(input("Preço: "))

    # valida preço
    if preco.isnumeric():
        preco = float(preco)

    preferencia =  str(input("Preferência: "))

    # verifica se preco esta preenchido corretamente
    while preferencia != ['sol', 'Sol', 'Sombra', 'sombra']:
        print('Digite uma preferencia válida! [sol ou sombra]')    
        preferencia =  str(input("Preferência: "))


    produto = [nome, preco, preferencia]
    return produto
