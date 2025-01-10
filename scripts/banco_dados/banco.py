import sqlite3
from servicos.funcoes_dados import recebe_dados

##########################################################################
#
#                      RECEBE DADOS PARA O BANCO
#
##########################################################################
def receber_dados_bd():    
    try:
        resultado = [*recebe_dados()]
    except(KeyboardInterrupt):
        print('Interrompido pelo teclado!')

    return resultado
##########################################################################
#
#                    INSERE PLANTAS NO BANCO DE DADOS
#
##########################################################################
def cadastrar_planta_db():
    conexao = sqlite3.connect('teste.db')

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
        
#########################################################################
#
#                           SELECIONA * PLANTAS
#                           
#########################################################################
def mostrar_plantas_db():
    conexao = sqlite3.connect('teste.db')

    cursor = conexao.execute("SELECT ID, NOME, PRECO, PREFERENCIA FROM PLANTA")
    for linha in cursor:
        print('----------------------')
        print('ID = ', linha[0])
        print('NOME = ', linha[1])
        print('PRECO = ', linha[2])

    print('Consulta realizado com sucesso!!')    


    
##########################################################################
#
#           TENTAR CONECTAR AO BANCO SE EXISTIR, SENÃO CRIA
#
##########################################################################
if __name__ == '__main__':
    conexao = sqlite3.connect('teste.db')
    print('Database criado com sucesso!')
##########################################################################
#
#                  VERIFICA SE A TABELA JA FOI CRIADA
#
##########################################################################
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


#########################################################################
#
#                             ENCERRA CONEXÃO
#                             
##########################################################################
    conexao.close()
##########################################################################
