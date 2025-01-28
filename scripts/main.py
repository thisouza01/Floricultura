# PROGRAMA PRINCIPAL
try:
    from menu import funcoes as funcao
    from time import sleep

    while True:
        funcao.mostra_interface('REGISTRAR')

        # zera a escolha 
        escolha = 0
        # lista de opçoes
        opçoes = [1, 2, 3, 4, 5, 6]

        # escolhe e valida opções'
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
            from gerenciamento.funcoes import cadastrar_planta_db

            # adiciona planta ao banco de dados
            cadastrar_planta_db(conexao = 'teste.db')
            # espera 1 segundo
            sleep(1)
            

#                          LISTAR TODAS AS PLANTAS

        elif escolha == 2: 
            from gerenciamento.funcoes import mostrar_todas_plantas_db, mostra_uma_planta_db

            # recebe escolha
            opçao = str(input('1 - Todas as plantas\n2 - Uma planta\n -> '))

            # verifica se é numérico
            if opçao.isnumeric():
                opçao = int(opçao)
            else:
                print('Tem que ser numérico! ')

            while opçao not in (1, 2):
                print('Digite uma opção válida')
                print()
                opçao = str(input('1 - Todas as plantas\n2 - Uma planta\n-> '))


            if opçao == 1:
                funcao.mostra_cabecalho('SELECIONANDO...')

                # seleciona as plantas no banco de dados
                mostrar_todas_plantas_db(conexao = r'C:\Users\tihso\Floricultura\scripts\teste.db')
            else:    
                funcao.mostra_cabecalho('SELECIONANDO...')

                # seleciona apenas uma planta pelo nome no banco de dados 
                mostra_uma_planta_db(conexao = r'C:\Users\tihso\Floricultura\scripts\teste.db')

            # espera 1 segundo
            sleep(1)

#                         CONVERTE PARA ARQUIVO
              
        elif escolha == 3: 
            from conversao.converter_arquivo import escreve_arquivo
            
            funcao.mostra_cabecalho('CONVERTENDO...')

            escreve_arquivo(conexao = r'C:\Users\tihso\Floricultura\scripts\teste.db')  
            # espera 1 segundo
            sleep(1)

#                         ATUALIZA DADO DAS PLANTAS
              
        elif escolha == 4: 
            from gerenciamento.funcoes import atualizar_planta_db

            funcao.mostra_cabecalho('ATUALIZANDO...')
            
            atualizar_planta_db(conexao = r'C:\Users\tihso\Floricultura\scripts\teste.db')  
            # espera 1 segundo
            sleep(1)

#                         DELETA DADO DAS PLANTAS QUE SÂO NULOS
              
        elif escolha == 5: 
            from gerenciamento.funcoes import deleta_planta_db

            funcao.mostra_cabecalho('EXCLUINDO...')
            
            deleta_planta_db(conexao = r'C:\Users\tihso\Floricultura\scripts\teste.db')  
            # espera 1 segundo
            sleep(1)

#                              SAIDA
           
        elif escolha == 6:
            break
        else:
            print('Opção inválida, digite outra')
            
except KeyboardInterrupt:
    print('\nPrograma cancelado via teclado!')