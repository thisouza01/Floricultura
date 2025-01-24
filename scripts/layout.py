from tkinter import *
from tkinter import ttk
from banco_dados.banco import deleta_planta_db


# cria uma nova instancia Tcl
root = Tk()

# cria um widget Frame
frm = ttk.Frame(root, padding=10)

# ajusta o Frame a janela root
frm.grid()

converter = deleta_planta_db(r'C:\Users\tihso\OneDrive\Área de Trabalho\Floricultura\Floricultura-18\scripts\teste.db')

# cria uma Label que contem o texto Hello World!
ttk.Button(frm, text='converter', command=converter).grid(column=0, row=0)

# cria um botal que sai da janela
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)

# precisa de um loop para rodar a janela
root.mainloop()