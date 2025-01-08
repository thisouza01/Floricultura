import pandas as pd

# recebe dados
def recebe_dados():
    nome =  str(input("Nome da planta: "))
    preco =  float(input("Preço: "))
    preferencia =  str(input("Preferência: "))

    produto = [nome, preco, preferencia]
    return produto

# adicionar novas plantas
def adicionar_planta():
    import classes.classe_Planta as classe_Planta

    global tabela

    # recebe os dados
    dados = recebe_dados()

    # adiciona nova planta
    nova_planta = classe_Planta.Planta(*dados)
    nova_planta_dic = nova_planta.dicionario()

    # atualiza a tabela
    tabela = pd.concat([tabela, pd.DataFrame([nova_planta_dic])], ignore_index=True)
    tabela.to_excel(r"C:\Users\WIN 11\OneDrive\Desktop\OneDrivethiago\OneDrive\Excel-Python\Floricultura - Copiar.xlsx", index=False)