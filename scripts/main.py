# PROGRAMA PRINCIPAL
try:
    from menu import funcoes as funcao

    while True:
        funcao.mostra_interface('REGISTRAR')

        # zera a escolha 
        escolha = 0
        # lista de opçoes
        opçoes = [1, 2, 3, 4, 5, 6]

        # escolhe e valida opções
        while escolha not in (opçoes):
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

            funcao.mostra_cabecalho('SELECIONANDO...')

            # seleciona as plantas no banco de dados
            mostrar_plantas_db(conexao = r'C:\Users\tihso\OneDrive\Área de Trabalho\Floricultura\Floricultura-11\scripts\teste.db')
 

#                         CONVERTE PARA ARQUIVO
              
        elif escolha == 3: 
            import conversao.converter_arquivo as convert_arq
            
            convert_arq.escreve_arquivo(conexao = r'C:\Users\tihso\OneDrive\Área de Trabalho\Floricultura\Floricultura-11\scripts\teste.db')  
            

#                         ATUALIZA DADO DAS PLANTAS
              
        elif escolha == 4: 
            from banco_dados.banco import atualizar_planta_db
            
            atualizar_planta_db(conexao = r'C:\Users\tihso\OneDrive\Área de Trabalho\Floricultura\Floricultura-11\scripts\teste.db')  


#                         DELETA DADO DAS PLANTAS QUE SÂO NULOS
              
        elif escolha == 5: 
            from banco_dados.banco import deleta_planta_db
            
            deleta_planta_db(conexao = r'C:\Users\tihso\OneDrive\Área de Trabalho\Floricultura\Floricultura-11\scripts\teste.db')  


#                              SAIDA
           
        elif escolha == 6:
            break
        else:
            print('Opção inválida, digite outra')
            
except KeyboardInterrupt:
    print('\nPrograma cancelado via teclado!')