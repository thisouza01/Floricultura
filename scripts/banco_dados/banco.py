import sqlite3
from servicos.funcoes_dados import recebe_dados

#                      RECEBE DADOS PARA O BANCO

def receber_dados_bd():    
    try:
        resultado = [*recebe_dados()]
   
    except(KeyboardInterrupt):
        print('Interrompido pelo teclado!')

    return resultado

#                    INSERE PLANTAS NO BANCO DE DADOS

def cadastrar_planta_db(conexao):
    # dados ja vem validados
    resultado = recebe_dados()
    
    nome_db = resultado[0]
    preco_db = resultado[1]
    preferencia_db = resultado[2]
    
    if len(resultado) != 3:
        raise ValueError('A função deve retornar apenas 3 argumentos: ')

    query = """
            INSERT INTO PLANTA (NOME,PRECO,PREFERENCIA)
            VALUES (?,?,?)
        """
    try:
        # Insere os dados
        conexao.execute(query, (nome_db, preco_db, preferencia_db))
        conexao.commit()
        print('-'*20)
        print("Dados inseridos com sucesso!")
    except sqlite3.Error as e:
        print("Erro ao inserir dados no banco de dados:", e)
    

#                           SELECIONA * PLANTAS

def mostrar_plantas_db(conexao):

    with sqlite3.connect(conexao) as conecta:

        # me possibilita acessar os dados como um dicionário - pelos nomes
        conecta.row_factory = sqlite3.Row

        cursor = conecta.execute("SELECT ID, NOME, PRECO, PREFERENCIA FROM PLANTA")

        for linha in cursor:
            print('-'*80)
            print('ID = ', linha['ID'], end = ' | ')
            print('NOME = ', linha['NOME'], end = ' | ')
            print('PRECO = ', linha['PRECO'], end = ' | ')
            print('PREFERENCIA = ', linha['PREFERENCIA'])

        print('Consulta realizado com sucesso!!')     


#           TENTAR CONECTAR AO BANCO SE EXISTIR, SENÃO CRIA

if __name__ == '__main__':
    conexao = sqlite3.connect('teste.db')
    print('Database criado com sucesso!')

#                  VERIFICA SE A TABELA JA FOI CRIADA

    recebe_cursor = conexao.execute('''SELECT COUNT(*) from sqlite_master''')
    qnt_tabelas = recebe_cursor.fetchone()[0]

    if qnt_tabelas == 0:
        # criar uma tabela
        conexao.execute(''' CREATE TABLE PLANTA
                        (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                        NOME TEXT              NOT NULL,
                        PRECO REAL             NOT NULL,
                        PREFERENCIA TEXT       NOT NULL);''')
        print('Tabela criada com sucesso!')


    cadastrar_planta_db()
    mostrar_plantas_db()


#                             ENCERRA CONEXÃO

    conexao.close()
