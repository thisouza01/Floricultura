# mostra uma linha
def mostra_linha():
    print("="*28)

# menu para receber dados
def mostra_cabecalho():
    mostra_linha()
    print("       REGISTRAR       ")
    mostra_linha()

def mostra_interface():
    # Coloca o cabeçalho
    mostra_cabecalho()

    # Mostra as opções
    print('1 - Adicionar planta')
    print('2 - Listagem de plantas')
    print('3 - Converter arquivo para CSV ou Excel')
    print('4 - Sair')

    mostra_linha()