
#########################################################################
#
#                         ESCREVE NO ARQUIVO TXT
#                           
#########################################################################
def escreve_arquivo():
    import sqlite3
    conexao = sqlite3.connect(r'C:\Users\WIN 11\Floricultura\Floricultura-4\scripts\teste.db')
    
    cursor = conexao.execute("SELECT ID, NOME, PRECO, PREFERENCIA FROM PLANTA")
    dados = cursor.fetchall()
    
    with open("tabela_plantas.txt", 'w', encoding="utf-8") as arquivo:
        arquivo.write("ID|Nome    |   Preço  |     Preferencia    \n")
        arquivo.write("-" * 80 + "\n")
        
        for linha in dados:
            id, nome, preco, preferencia = linha
            arquivo.write(f'{id};{nome};{preco};{preferencia}\n')

    print('Convertido com sucesso!!')

if __name__ == '__main__':
    escreve_arquivo()    