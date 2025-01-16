# mostra uma linha
def mostra_linha():
    print("="*28)

# menu para receber dados
def mostra_cabecalho(nome):
    mostra_linha()
    print(f"       {nome}       ")
    mostra_linha()

def mostra_interface(nome):
    # Coloca o cabeçalho
    mostra_cabecalho(nome)

    # Mostra as opções
    print('1 - Adicionar planta')
    print('2 - Listagem de plantas')
    print('3 - Converter arquivo para TXT')
    print('4 - Atualizar dados das plantas')
    print('5 - Sair')

    mostra_linha()   