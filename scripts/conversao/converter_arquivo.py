
def converte_arquivo(tabela, formato = 'csv'):
    from main import tabela

    if formato.lower() == 'csv':
        tabela.to_csv('floricultura.csv', index=False, sep='|')
        print("Arquivo exportado como CSV com sucesso!") 

    elif formato.lower() == 'excel':
        tabela.to_excel('floricultura.xlsx', index=False)    
        print("Arquivo exportado como Excel com sucesso!") 

    else:
        print("Formato não suportado. Escolha 'csv' ou 'excel'.")