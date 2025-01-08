import sqlite3

# tentar conectar ao banco de dados teste.db -> se não existir, cria
conexao = sqlite3.connect('teste.db')
print('Database criado com sucesso!')

# criar uma tabela
conexao.execute(''' CREATE TABLE PLANTA
                (ID INT PRIMARY KEY     NOT NULL,
                 NOME TEXT              NOT NULL,
                 PRECO REAL             NOT NULL);''')
print('Tabela criada com sucesso!')

# insere dados
conexao.execute("INSERT INTO PLANTA (ID,NOME,PRECO) \
                      VALUES (1, 'Zamiokulka G', '80')");

conexao.execute("INSERT INTO PLANTA (ID,NOME,PRECO) \
                      VALUES (2, 'Zamiokulka P', '80')");

# commit para salvar
conexao.commit()
print('Arquivos inseridos com sucesso!!')

# selecionar produtos
cursor = conexao.execute("SELECT  ID, NOME, PRECO FROM PLANTA")
for linha in cursor:
    print('ID = ', linha[0])
    print('NOME = ', linha[1])
    print('PRECO = ', linha[2])

print('Consulta realiado com sucesso!!')    

# encerra conexao
conexao.close()