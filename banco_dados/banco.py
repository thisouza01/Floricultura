import sqlite3
from scripts.servicos.funcoes_dados import *

# tentar conectar ao banco de dados teste.db -> se não existir, cria
conexao = sqlite3.connect('teste.db')
print('Database criado com sucesso!')

# criar uma tabela
conexao.execute(''' CREATE TABLE PLANTA
                (ID INT PRIMARY KEY     NOT NULL,
                 NOME TEXT              NOT NULL,
                 PRECO REAL             NOT NULL,
                 PREFERENCIA TEXT       NOT NULL);''')
print('Tabela criada com sucesso!')

resultado = [recebe_dados()]

if len(resultado) != 3:
    raise ValueError('A função deve retornar apenas 3 argumentos: ')

query = """
        INSERT INTO PLANTA (ID,NOME,PRECO,PREFERENCIA)
        VALUES (?,?,?,?)
    """
try:
    # Insere os dados
    conexao.execute(query, (id, resultado[0], resultado[1], resultado[2]))
    conexao.commit()
    print("Dados inseridos com sucesso!")
except sqlite3.Error as e:
    print("Erro ao inserir dados no banco de dados:", e)
        
# selecionar produtos
cursor = conexao.execute("SELECT  ID, NOME, PRECO FROM PLANTA")
for linha in cursor:
    print('ID = ', linha[0])
    print('NOME = ', linha[1])
    print('PRECO = ', linha[2])

print('Consulta realiado com sucesso!!')    

# encerra conexao
conexao.close()