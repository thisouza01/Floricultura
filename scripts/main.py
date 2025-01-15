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

#                          CADASTRA AS PLANTAS

        if escolha == 1: 
            from banco_dados.banco import cadastrar_planta_db
            import sqlite3

            # adiciona planta ao banco de dados
            cadastrar_planta_db(conexao = sqlite3.connect('teste.db'))
            
            # encerra conexão
            conexao.close()
            print("Conexão encerrada com sucesso.")

#                          LISTA AS PLANTAS

        elif escolha == 2: 
            from banco_dados.banco import mostrar_plantas_db
            import sqlite3

            funcao.mostra_cabecalho('SELECIONANDO...')

            # passo o caminho do bancoa de dados 
            conexao = r'C:\Users\WIN 11\Floricultura\Floricultura-5\scripts\teste.db'
            
            mostrar_plantas_db(conexao)

            

#                         CONVERTE PARA ARQUIVO
              
        elif escolha == 3: 
            import conversao.converter_arquivo as convert_arq
            import sqlite3

            # abro a conexão
            conexao = sqlite3.connect(r'C:\Users\WIN 11\Floricultura\Floricultura-5\scripts\teste.db')

            convert_arq.escreve_arquivo(conexao)  
            
#                              SAIDA
           
        elif escolha == 4:
            break
        else:
            print('Opção inválida, digite outra')
            
except KeyboardInterrupt:
    print('\nPrograma cancelado via teclado!')