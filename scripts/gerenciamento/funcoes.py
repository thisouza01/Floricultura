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

        with sqlite3.connect(conexao) as conecta:
            # Insere os dados
            conecta.execute(query, (nome_db, preco_db, preferencia_db))
            print('-'*20)
            print("Dados inseridos com sucesso!")

    except sqlite3.Error as e:
        print("Erro ao inserir dados no banco de dados:", e)

    except sqlite3.ProgrammingError:
        print('Banco de dados não acessível!')   
    

#                           SELECIONA * PLANTAS

def mostrar_todas_plantas_db(conexao):
    import tkinter as tk
    from tkinter import ttk

    try:
        with sqlite3.connect(conexao) as conecta:

            # me possibilita acessar os dados como um dicionário - pelos nomes
            conecta.row_factory = sqlite3.Row
            cursor = conecta.execute("SELECT ID, NOME, PRECO, PREFERENCIA FROM PLANTA ORDER BY ID")

            # limpa a lista antes de adicionar novos itens
            tk.Listbox.delete(0, tk.END)

            # adiciona a listbox
            for linha in cursor:
                tk.Listbox.insert(tk.END, f"{linha['ID']} - {linha['NOME']} | R$ {linha['PRECO']} | {linha['PREFERENCIA']}")

            print('Plantas carregadas com sucesso!')   
              
    except sqlite3.Error as e:
        print("Erro ao atualizar dados no banco de dados:", e)

    except sqlite3.ProgrammingError:
        print('Banco de dados não acessível!')

#                           SELECIONA 1 PLANTAS

def mostra_uma_planta_db(conexao):
    from menu.funcoes import row_formatada

    try:
        with sqlite3.connect(conexao) as conecta:

            conecta.row_factory = sqlite3.Row

            nome_planta = str(input('Qual o nome da planta que deseja ver?\n-> '))

            cursor = conecta.execute("""
                                     SELECT ID, NOME, PRECO, PREFERENCIA
                                     FROM PLANTA
                                     WHERE NOME = ?
                                    """,(nome_planta.capitalize(),))
            
            linha = cursor.fetchone()
            
            if linha:
                row_formatada(linha)
            else:
                print(f'Planta {nome_planta} não encontrada!')

            
        

    except sqlite3.Error as e:
        print("Erro ao mostrar dados no banco de dados:", e)

    except sqlite3.ProgrammingError:
        print('Banco de dados não acessível!')
            

#                           ATUALIZA DADOS PLANTAS

def atualizar_planta_db(conexao):

    # gostaria de atualizar qual planta?

    try:

        escolha = str(input('Quer atualizar oque?\n1 - Nome\n2 - Preço\n3 - Preferência\n--> '))
    
        match escolha:

            case '1':
            
                with sqlite3.connect(conexao) as conecta:

                    id_planta = int(input('Qual o id da planta para atualizar: '))
                    novo_nome = str(input('Nome atualizado: '))

                    conecta.execute("""
                                    UPDATE PLANTA
                                    SET NOME = ?
                                    WHERE ID = ? 
                                    """,(novo_nome.capitalize(), id_planta))
            

            case '2':
                
                with sqlite3.connect(conexao) as conecta:
                    
                    id_planta = int(input('Qual o id da planta para atualizar: '))
                    novo_preco = str(input('Preço atualizado: '))
                    
                    conecta.execute("""
                                    UPDATE PLANTA
                                    SET PRECO = ?
                                    WHERE ID = ? 
                                    """,(novo_preco, id_planta))

            case '3':

                with sqlite3.connect(conexao) as conecta:
                    
                    id_planta = int(input('Qual o id da planta para atualizar: '))
                    nova_preferencia = str(input('Preferência atualizado: '))
                    
                    conecta.execute("""
                                    UPDATE PLANTA
                                    SET PREFERENCIA = ?
                                    WHERE ID = ? 
                                    """,(nova_preferencia, id_planta))

            case _:
                return f"ID {id_planta} inválido!"
                            
            
        print('Atualizado com sucesso!!')

    except sqlite3.Error as e:
        print("Erro ao atualizar dados no banco de dados:", e)

    except sqlite3.ProgrammingError:
        print('Banco de dados não acessível!')

    except (ValueError, TypeError):
        print('')    


#                           DELETA DADOS NULOS PLANTAS

def deleta_planta_db(conexao):
    try:

        with sqlite3.connect(conexao) as conecta:

            #conecta.execute("DELETE FROM PLANTA WHERE NOME IS NULL OR NOME = ''" )
            conecta.execute("DELETE FROM PLANTA WHERE NOME = 666")

        print('Deletado com sucesso!')

    except sqlite3.Error as e:
        print("Erro ao atualizar dados no banco de dados:", e)

    except sqlite3.ProgrammingError:
        print('Banco de dados não acessível!')

