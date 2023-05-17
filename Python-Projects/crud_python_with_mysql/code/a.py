import tkinter as tk

window = tk.Tk()

# Criar a barra de rolagem
scrollbar = tk.Scrollbar(window)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Criar a lista
lista = tk.Listbox(window, yscrollcommand=scrollbar.set)
lista.pack(side=tk.LEFT, fill=tk.BOTH)

# Vincular a barra de rolagem à lista
scrollbar.config(command=lista.yview)

# Adicionar itens à lista
for i in range(100):
    lista.insert(tk.END, f"Item {i}")

window.mainloop()