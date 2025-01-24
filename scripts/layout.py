from tkinter import *
from tkinter import ttk
from banco_dados.banco import * 


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
    command=lambda: cadastrar_planta_db(r'C:\Users\WIN 11\OneDrive\Desktop\Floricultura\Floricultura-7\scripts\teste.db')).grid(column=0, row=0)

# BOTAO PARA LISTAR TODAS AS PLANTA
ttk.Button(
    frm,
    text='Listar todas',
    command=lambda: mostrar_todas_plantas_db(r'C:\Users\WIN 11\OneDrive\Desktop\Floricultura\Floricultura-7\scripts\teste.db')).grid(column=0, row=1)

# BOTAO PARA LISTAR UMA PLANTA
ttk.Button(
    frm,
    text='Listar uma',
    command=lambda: mostra_uma_planta_db(r'C:\Users\WIN 11\OneDrive\Desktop\Floricultura\Floricultura-7\scripts\teste.db')).grid(column=0, row=2)

# BOTAO PARA ATUALIZAR UMA PLANTA
ttk.Button(
    frm,
    text='Atualizar',
    command=lambda: atualizar_planta_db(r'C:\Users\WIN 11\OneDrive\Desktop\Floricultura\Floricultura-7\scripts\teste.db')).grid(column=0, row=3)


# cria um botal que sai da janela
ttk.Button(
    frm,
    text="Quit",
    command=root.destroy).grid(column=3, row=0)

# precisa de um loop para rodar a janela
root.mainloop()