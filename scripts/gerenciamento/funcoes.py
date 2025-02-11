import sqlite3
import tkinter as tk
from servicos.funcoes_dados import recebe_dados
from layout import cad_nome_planta, cad_preco_planta, cad_preferencia_planta

#                      RECEBE DADOS PARA O BANCO

def receber_dados_bd():    
    # recebe dados via TKinter
    nome = cad_nome_planta.get().strip()
    preco = cad_preco_planta.get().strip()
    preferencia = cad_preferencia_planta.get().strip()

    try:
        preco = float(preco)

    except(KeyboardInterrupt):
        print('Interrompido pelo teclado!')
    except(ValueError, TypeError):
        print('Preço deve ser um numero válido')


    return nome, preco, preferencia


#                    INSERE PLANTAS NO BANCO DE DADOS

def cadastrar_planta_db(conexao):
    resultado = recebe_dados()
    
    if resultado is None:
        return 
    
    # validar dados



    nome_db, preco_db, preferencia_db = resultado
    
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

def mostrar_todas_plantas_db(conexao, listbox):
    try:
        with sqlite3.connect(conexao) as conecta:

            # me possibilita acessar os dados como um dicionário - pelos nomes
            conecta.row_factory = sqlite3.Row
            cursor = conecta.execute("SELECT ID, NOME, PRECO, PREFERENCIA FROM PLANTA ORDER BY ID")
            plantas = cursor.fetchall()

            # limpa a lista antes de adicionar novos itens
            listbox.delete(0, tk.END)

            # adiciona a listbox
            for planta in plantas:
                listbox.insert(tk.END, f"{planta['ID']} - {planta['NOME']} | R$ {planta['PRECO']} | {planta['PREFERENCIA']}")

            # Ajustar a altura do listbox conforme o número de itens
            listbox.config(height=len(plantas) if len(plantas) > 0 else 1)

            print('Plantas carregadas com sucesso!')   
              
    except sqlite3.Error as e:
        print("Erro ao atualizar dados no banco de dados:", e)

    except sqlite3.ProgrammingError:
        print('Banco de dados não acessível!')

#                           SELECIONA 1 PLANTAS

def mostra_uma_planta_db(conexao, nome_planta, resultado_label):
    if resultado_label is None: 
        print("Erro: resultado_label não foi passado corretamente!")
        return

    try:
        with sqlite3.connect(conexao) as conecta:

            conecta.row_factory = sqlite3.Row

            cursor = conecta.execute("""
                                     SELECT NOME, PRECO, PREFERENCIA
                                     FROM PLANTA
                                     WHERE NOME = ?
                                    """,(nome_planta,))
            
            linha = cursor.fetchone()
            
            if linha:
                resultado = f"Nome: {linha['NOME']}\n Preço: R${linha['PRECO']}\n Preferência: {linha['PREFERENCIA']}"
                resultado_label.config(text=resultado)
            else:
                resultado_label.config(text=f'Planta "{nome_planta}" não encontrada!')
                
    except sqlite3.Error as e:
        print("Erro ao mostrar dados no banco de dados:", e)

    except Exception as e:
        resultado_label.config(text=f"Erro: {str(e)}", fg="red")

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

