# recebe dados
def recebe_dados():

    # valida os dados
    def entrada_valida(mensagem, validacao, msg_erro):
        # loop para verificação
        while True:
            valor = input(mensagem).strip()
            if validacao(valor):
                return valor
            print(msg_erro)


    # valida o nome
    nome = entrada_valida(
        'Nome da planta: ',
        # o tamanho do nome tem que ser maior que 2
        lambda x: len(x) > 2 and str(x).isalpha(),
        'Deve conter no mínimo 3 caracteres alfabeticos!'
    )

    # valida 0 preço
    preco = entrada_valida(
        'Preço: ',
        # troco o ponto e verifico se são todos numeros
        lambda x: str(x).replace('.', '', 1).isdigit(),
        'Preço inválido! Digite um valor numérico.'
    )
    # converte para float o numero
    preco = float(preco)

    # Validação para a preferência
    preferencia = entrada_valida(
        "Preferência [sol ou sombra]: ",
        lambda x: str(x).lower() in ['sol', 'sombra'],
        "Preferência inválida! Digite 'sol' ou 'sombra'."
    )
    preferencia = preferencia.lower()

    produto = [nome, preco, preferencia]
    return produto
