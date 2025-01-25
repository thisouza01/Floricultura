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

    # o tamanho do nome tem que ser maior que 2, pode conter espaço e não pode ser numero
    def valida_nome(nome):
        return len(nome) > 2 and all(char.isalpha() or char.isspace() for char in nome)


    # valida o nome
    nome = entrada_valida(
        'Nome da planta: ',
        valida_nome,
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

    produto = [nome.capitalize(), preco, preferencia]
    return produto
