# PROGRAMA PRINCIPAL
try:
    from menu import funcoes as funcao

    while True:
        funcao.mostra_interface('REGISTRAR')

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
            from banco_dados.banco import cadastrar_planta_db

            # adiciona planta ao banco de dados
            cadastrar_planta_db()

        elif escolha == 2: # MOSTRA AS PLANTAS
            import pandas as pd
            from banco_dados.banco import mostrar_plantas_db


            # escolha qual versão ver
            escolha_lista = str(input('1 - Arquivo\n2 - Tabela do banco de dados \n--> '))

            funcao.mostra_cabecalho('SELECIONANDO')

            # verifica escolha
            if escolha_lista.isnumeric() and (escolha_lista == '1' or escolha_lista == '2'):
                escolha_lista = int(escolha_lista)
            else:
                print('Escolha uma opção válida!!')    

            if escolha_lista == 1:
                # carregar dados do excel
                tabela = pd.read_excel(r"C:\Users\WIN 11\OneDrive\Desktop\OneDrivethiago\OneDrive\Excel-Python\Floricultura - Copiar.xlsx")

                # ordenar por nome
                tabela = tabela.sort_values(by="Nome")

                # salvar alteração
                tabela.to_excel(r"C:\Users\WIN 11\OneDrive\Desktop\OneDrivethiago\OneDrive\Excel-Python\Floricultura - Copiar.xlsx", index=False)
                
                # exibe os dados
                print(tabela)  
            else:
                mostrar_plantas_db()
                
        elif escolha == 3: # CONVERTE O ARQUIVO
            import conversao.converter_arquivo as convert_arq

            convert_arq.escreve_arquivo()  
            
        elif escolha == 4:
            break
        else:
            print('Opção inválida, digite outra')
            
except KeyboardInterrupt:
    print('\nPrograma cancelado via teclado!')