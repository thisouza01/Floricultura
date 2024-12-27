import pandas as pd

# carregar dados do excel
tabela = pd.read_excel(r"C:\Users\WIN 11\OneDrive\Desktop\OneDrivethiago\OneDrive\Excel-Python\Floricultura - Copiar.xlsx")

# recebe dados
def recebe_dados():
    nome =  str(input("Nome da planta: "))
    preco =  float(input("Preço: "))
    preferencia =  str(input("Preferência: "))

    produto = [nome, preco, preferencia]
    return produto

# adicionar novas plantas
def adicionar_planta():
    import classes.classe_Planta as classe_Planta

    global tabela

    # recebe os dados
    dados = recebe_dados()

    # adiciona nova planta
    nova_planta = classe_Planta.Planta(*dados)
    nova_planta_dic = nova_planta.dicionario()

    # atualiza a tabela
    tabela = pd.concat([tabela, pd.DataFrame([nova_planta_dic])], ignore_index=True)
    tabela.to_excel(r"C:\Users\WIN 11\OneDrive\Desktop\OneDrivethiago\OneDrive\Excel-Python\Floricultura - Copiar.xlsx", index=False)

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

if __name__ == '__main__':
    # PROGRAMA PRINCIPAL
    while True:
        mostra_interface()

        # zera a escolha 
        escolha = 0

        while escolha not in (1, 2, 3, 4):
            # verifica se quer adicionar
            escolha = str(input("Escolha a opção: ").strip())

            if escolha.isnumeric():
                escolha = int(escolha)
            else:    
                print('Digite uma opção válida!')
            
        mostra_linha() 


        if escolha == 1:
            adicionar_planta()
        elif escolha == 2:
            # ordenar por nome
            tabela = tabela.sort_values(by="Nome")
            # salvar alteração
            tabela.to_excel(r"C:\Users\WIN 11\OneDrive\Desktop\OneDrivethiago\OneDrive\Excel-Python\Floricultura - Copiar.xlsx", index=False)
            # exibe os dados
            print(tabela)  
        elif escolha == 3:
            import conversao.converter_arquivo as convert_arq

            # recebe a escolha
            escolha_convert = str(input('1 - Excel \n2 - CSV \n'))

            # verifica se é numerico
            if escolha_convert.isnumeric() and '1' == escolha_convert == '2':
                escolha_convert = int(escolha_convert)
            else:
                print('Digite uma opção válida!')

            if escolha_convert == 1:
                # converte para Excel
                convert_arq.converte_arquivo(tabela, formato='Excel')
            else:
                # converte para CSV
                convert_arq.converte_arquivo(tabela, formato='CSV')    
        elif escolha == 4:
            break
        else:
            print('Opção inválida, digite outra')
