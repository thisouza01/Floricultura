from tkinter import *
from tkinter import ttk
from banco_dados.banco import * 
from conversao.converter_arquivo import escreve_arquivo

# esconde todos so frames e mostra apenas o selecionado
def mostrar_frame(frm):
    frm1.grid_forget()
    frm2.grid_forget()
    frm3.grid_forget()
    frm4.grid_forget()
    frm.grid(row=0, column=0, sticky="nsew")

# cria uma nova instancia Tcl
root = Tk()
root.title('Tela Principal')
root.geometry('700x400')

# cria um frame principal
frm1 = ttk.Frame(root, padding=10)
frm1.grid(row=0, column=0, sticky="nsew")

# cria o segundo Frame para listar as plantas
frm2 = ttk.Frame(root, padding=10)

# cria o segundo Frame para listar uma plantas
frm3 = ttk.Frame(root, padding=10)

# cria o segundo Frame para listar uma plantas
frm4 = ttk.Frame(root, padding=10)

# Listbox para exibir as plantas
listbox = Listbox(frm3, width=40)
listbox.grid(column=0, row=0, padx=10, pady=10)



# BOTÃO PARA VOLTAR PARA O FRAME1
ttk.Button(
    frm2,
    text='Voltar',
    command=lambda: mostrar_frame(frm1)).grid(column=0, row=5, pady=10)

ttk.Button(
    frm3,
    text='Voltar',
    command=lambda: mostrar_frame(frm1)).grid(column=0, row=5, pady=10)

ttk.Button(
    frm4,
    text='Voltar',
    command=lambda: mostrar_frame(frm1)).grid(column=0, row=5, pady=10)


# BOTAO PARA ADICIONAR UMA PLANTA
ttk.Button(
    frm1,
    text='Adicionar',
    command=lambda: [mostrar_frame(frm4), cadastrar_planta_db(r'C:\Users\WIN 11\Floricultura-3\scripts\teste.db')]).grid(column=0, row=0)

lbl_nome_cadastro = tk.Label(frm4, text='Nome da planta')
lbl_nome_cadastro.grid(row=0, column=0, padx=5, pady=5)

nome_planta_cad = tk.StringVar() 

# BOTAO PARA LISTAR TODAS AS PLANTA
ttk.Button(
    frm1,
    text='Listar todas',
    command=lambda: [mostrar_frame(frm3), mostrar_todas_plantas_db(conexao=r'C:\Users\WIN 11\Floricultura-3\scripts\teste.db', listbox=listbox)]).grid(column=0, row=1)

 


# LISTAR UMA PLANTA

# cria a label
lbl_nome = tk.Label(frm2, text='Nome da planta')
lbl_nome.grid(row=0, column=0, padx=5, pady=5)

# cria a entrada
nome_planta_var = tk.StringVar()
nome_planta = tk.Entry(frm2, textvariable=nome_planta_var)
nome_planta.grid(row=0, column=1, padx=5, pady=5)

ttk.Button(
    frm1,
    text="Listar uma",
    command=lambda: mostrar_frame(frm2)
).grid(column=0, row=2)

resultado_label = tk.Label(frm2, text='')
resultado_label.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

ttk.Button(
    frm2,
    text='Buscar',
    command = lambda: mostra_uma_planta_db(
                                            conexao=r'C:\Users\WIN 11\Floricultura-3\scripts\teste.db',
                                            nome_planta=nome_planta_var.get().strip(),
                                            resultado_label=resultado_label)).grid(row=0, column=2, padx=5, pady=5)






# BOTAO PARA ATUALIZAR UMA PLANTA
ttk.Button(
    frm1,
    text='Atualizar',
    command=lambda: atualizar_planta_db(r'C:\Users\WIN 11\Floricultura-3\scripts\teste.db')).grid(column=0, row=3)

# BOTAO PARA CONVERTER ARQUIVO
ttk.Button(
    frm1,
    text='Converter para TXT',
    command=lambda: escreve_arquivo(r'C:\Users\WIN 11\Floricultura-3\scripts\teste.db')).grid(column=0, row=4)

# BOTAO PARA DELETAR PLANTA
ttk.Button(
    frm1,
    text='Excluir planta',
    command=lambda: deleta_planta_db(r'C:\Users\WIN 11\Floricultura-3\scripts\teste.db')).grid(column=0, row=5)


# cria um botal que sai da janela
ttk.Button(
    frm1,
    text="Quit",
    command=root.destroy).grid(column=3, row=0)

# precisa de um loop para rodar a janela
root.mainloop()