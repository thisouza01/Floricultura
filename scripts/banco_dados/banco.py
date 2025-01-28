import sqlite3
from gerenciamento.funcoes import *
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
    mostrar_todas_plantas_db()


#                             ENCERRA CONEXÃO

    conexao.close()
