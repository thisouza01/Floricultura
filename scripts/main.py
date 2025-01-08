import menu.funcoes as funcao

    # PROGRAMA PRINCIPAL
try:
    while True:
        funcao.mostra_interface()

        # zera a escolha 
        escolha = 0

        while escolha not in (1, 2, 3, 4):
            # verifica se quer adicionar
            escolha = str(input("Escolha a opção: ").strip())

            if escolha.isnumeric():
                escolha = int(escolha)
            else:    
                print('Digite uma opção válida!')
            
        funcao.mostra_linha() 


        if escolha == 1: # CADASTRA AS PLANTAS
            # import servicos.funcoes_dados as servico
            import banco_dados.banco as banco

            # adicionar planta ao arquivo
            # servico.adicionar_planta()

            # adiciona planta ao banco de dados
            banco.cadastrar_planta_db()

        elif escolha == 2: # MOSTRA AS PLANTAS
            import pandas as pd

            # carregar dados do excel
            tabela = pd.read_excel(r"C:\Users\WIN 11\OneDrive\Desktop\OneDrivethiago\OneDrive\Excel-Python\Floricultura - Copiar.xlsx")

            # ordenar por nome
            tabela = tabela.sort_values(by="Nome")

            # salvar alteração
            tabela.to_excel(r"C:\Users\WIN 11\OneDrive\Desktop\OneDrivethiago\OneDrive\Excel-Python\Floricultura - Copiar.xlsx", index=False)
            
            # exibe os dados
            print(tabela)  
        elif escolha == 3: # CONVERTE O ARQUIVO
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
            
except KeyboardInterrupt:
    print('Programa cancelado via teclado!')