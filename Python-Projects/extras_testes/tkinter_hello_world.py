# from tkinter import *
# from tkinter import ttk


# root = Tk()
# frm = ttk.Frame(root, padding=10)
# frm.grid()
# ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
# ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
# root.mainloop()


import tkinter as tk

janela = tk.Tk()

def on_click(event):
    if caixa_texto.get() == "Digite seu nome aqui":
        caixa_texto.delete(0, "end") # remove o texto explicativo

caixa_texto = tk.Entry(janela, width=30)
caixa_texto.insert(0, "Digite seu nome aqui")
caixa_texto.bind("<FocusIn>", on_click)
caixa_texto.pack()

janela.mainloop()