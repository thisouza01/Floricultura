from tkinter import *
from tkinter import ttk
from banco_dados.banco import * 
from conversao.converter_arquivo import escreve_arquivo

# esconde todos so frames e mostra apenas o selecionado
def mostrar_frame(frm):
    frm1.grid_forget()
    frm2.grid_forget()
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

# Listbox para exibir as plantas
listbox = Listbox(frm2, width=40)
listbox.grid(column=0, row=0, padx=10, pady=10)

# BOTÃO PARA VOLTAR PARA O FRAME1
ttk.Button(
    frm2,
    text='Voltar',
    command=lambda: mostrar_frame(frm1)).grid(column=0, row=1, pady=10)

# BOTAO PARA ADICIONAR UMA PLANTA
ttk.Button(
    frm1,
    text='Adicionar',
    command=lambda: cadastrar_planta_db(r'C:\Users\tihso\Floricultura-4\scripts\teste.db')).grid(column=0, row=0)


# BOTAO PARA LISTAR TODAS AS PLANTA
ttk.Button(
    frm1,
    text='Listar todas',
    command=lambda: [mostrar_frame(frm2), mostrar_todas_plantas_db(conexao=r'C:\Users\tihso\Floricultura-4\scripts\teste.db', listbox=listbox)]).grid(column=0, row=1)
 

# LISTAR UMA PLANTA

# cria a label
lbl_nome = tk.Label(frm2, text='Nome da planta')
lbl_nome.grid(row=0, column=0, padx=5, pady=5)

# cria a entrada
nome_planta = tk.Entry(frm2)
nome_planta.grid(row=0, column=1, padx=5, pady=5)

ttk.Button(
    frm1,
    text="Listar uma",
    command=lambda: mostrar_frame(frm2)
).grid(column=0, row=2)

ttk.Button(
    frm2,
    text='Buscar',
    command = lambda: mostra_uma_planta_db(conexao=r'C:\Users\tihso\Floricultura-4\scripts\teste.db', nome_planta=nome_planta.get())).grid(row=0, column=2, padx=5, pady=5)


# BOTAO PARA ATUALIZAR UMA PLANTA
ttk.Button(
    frm1,
    text='Atualizar',
    command=lambda: atualizar_planta_db(r'C:\Users\tihso\Floricultura-4\scripts\teste.db')).grid(column=0, row=3)

# BOTAO PARA CONVERTER ARQUIVO
ttk.Button(
    frm1,
    text='Converter para TXT',
    command=lambda: escreve_arquivo(r'C:\Users\tihso\Floricultura-4\scripts\teste.db')).grid(column=0, row=4)

# BOTAO PARA DELETAR PLANTA
ttk.Button(
    frm1,
    text='Excluir planta',
    command=lambda: deleta_planta_db(r'C:\Users\tihso\Floricultura-4\scripts\teste.db')).grid(column=0, row=5)


# cria um botal que sai da janela
ttk.Button(
    frm1,
    text="Quit",
    command=root.destroy).grid(column=3, row=0)

# precisa de um loop para rodar a janela
root.mainloop()