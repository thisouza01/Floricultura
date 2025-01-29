from tkinter import *
from tkinter import ttk
from banco_dados.banco import * 
from conversao.converter_arquivo import escreve_arquivo



# cria uma nova instancia Tcl
root = Tk()

# cria um widget Frame
frm = ttk.Frame(root, padding=10)

# ajusta o Frame a janela root
frm.grid()

# BOTAO PARA ADICIONAR UMA PLANTA
ttk.Button(
    frm,
    text='Adicionar',
    command=lambda: cadastrar_planta_db(r'C:\Users\tihso\Floricultura\scripts\teste.db')).grid(column=0, row=0)


# Listar todas as plantas


# BOTAO PARA LISTAR TODAS AS PLANTA
ttk.Button(
    frm,
    text='Listar todas',
    command=lambda: mostrar_todas_plantas_db(r'C:\Users\tihso\Floricultura\scripts\teste.db')).grid(column=0, row=1)
 



# BOTAO PARA LISTAR UMA PLANTA
ttk.Button(
    frm,
    text='Listar uma',
    command=lambda: mostra_uma_planta_db(r'C:\Users\tihso\Floricultura\scripts\teste.db')).grid(column=0, row=2)

# BOTAO PARA ATUALIZAR UMA PLANTA
ttk.Button(
    frm,
    text='Atualizar',
    command=lambda: atualizar_planta_db(r'C:\Users\tihso\Floricultura\scripts\teste.db')).grid(column=0, row=3)

# BOTAO PARA CONVERTER ARQUIVO
ttk.Button(
    frm,
    text='Converter para TXT',
    command=lambda: escreve_arquivo(r'C:\Users\tihso\Floricultura\scripts\teste.db')).grid(column=0, row=4)

# BOTAO PARA DELETAR PLANTA
ttk.Button(
    frm,
    text='Excluir planta',
    command=lambda: deleta_planta_db(r'C:\Users\tihso\Floricultura\scripts\teste.db')).grid(column=0, row=5)


# cria um botal que sai da janela
ttk.Button(
    frm,
    text="Quit",
    command=root.destroy).grid(column=3, row=0)

# precisa de um loop para rodar a janela
root.mainloop()