# PROGRAMA PRINCIPAL
try:
    from menu import funcoes as funcao

    while True:
        funcao.mostra_interface('REGISTRAR')

        # zera a escolha 
        escolha = 0

        # escolhe e valida opções
        while escolha not in (1, 2, 3, 4):
            # verifica se quer adicionar
            escolha = str(input("Escolha a opção: ").strip())

            if escolha.isnumeric():
                escolha = int(escolha)
            else:    
                print('Digite uma opção válida!')
        funcao.mostra_linha() 

#                          CADASTRA AS PLANTAS

        if escolha == 1: 
            from banco_dados.banco import cadastrar_planta_db

            # adiciona planta ao banco de dados
            cadastrar_planta_db(conexao = 'teste.db')
            

#                          LISTA AS PLANTAS

        elif escolha == 2: 
            from banco_dados.banco import mostrar_plantas_db
            import sqlite3

            funcao.mostra_cabecalho('SELECIONANDO...')

            # seleciona as plantas no banco de dados
            mostrar_plantas_db(conexao = r'C:\Users\WIN 11\Floricultura\Floricultura-5\scripts\teste.db')
 

#                         CONVERTE PARA ARQUIVO
              
        elif escolha == 3: 
            import conversao.converter_arquivo as convert_arq
            
            convert_arq.escreve_arquivo(conexao = r'C:\Users\WIN 11\Floricultura\Floricultura-5\scripts\teste.db')  
            
#                              SAIDA
           
        elif escolha == 4:
            break
        else:
            print('Opção inválida, digite outra')
            
except KeyboardInterrupt:
    print('\nPrograma cancelado via teclado!')