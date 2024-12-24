import pandas as pd

# carregar dados do excel
tabela = pd.read_excel(r"C:\Users\tihso\OneDrive\Excel-Python\Floricultura - Copiar.xlsx")

# recebe dados
def recebe_dados():
    nome =  str(input("Nome da planta: "))
    preco =  float(input("Preço: "))
    preferencia =  str(input("Preferência: "))

    produto = [nome, preco, preferencia]
    return produto

# adicionar novas plantas
def adicionar_planta():
    import classe_Planta

    global tabela

    # recebe os dados
    dados = recebe_dados()

    # adiciona nova planta
    nova_planta = classe_Planta.Planta(*dados)
    nova_planta_dic = nova_planta.dicionario()

    # atualiza a tabela
    tabela = pd.concat([tabela, pd.DataFrame([nova_planta_dic])], ignore_index=True)
    tabela.to_excel(r"C:\Users\tihso\OneDrive\Excel-Python\Floricultura - Copiar.xlsx", index=False)

# mostra uma linha
def mostra_linha():
    print("="*30)

# menu para receber dados
def mostra_cabecalho():
    mostra_linha()
    print("       REGISTRAR       ")
    mostra_linha()


# PROGRAMA PRINCIPAL
while True:
    mostra_cabecalho()

    # verifica se quer adicionar
    escolha = input("Quer adicionar uma nova planta? (s / n): ").strip().lower()
    mostra_linha()
    while escolha not in ('s', 'n'):
        print('Digite uma opção válida!')
        escolha = input("Quer adicionar uma nova planta? (s / n): ").strip().lower()
        mostra_linha()

    if escolha == 'n':
        break
    else:
        adicionar_planta()


# ordenar por nome
tabela = tabela.sort_values(by="Nome")
# salvar alteração
tabela.to_excel(r"C:\Users\tihso\OneDrive\Excel-Python\Floricultura - Copiar.xlsx", index=False)

# exibe os dados
print(tabela)