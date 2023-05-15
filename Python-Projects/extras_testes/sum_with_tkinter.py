import tkinter as tk

#Colocando texto placeholder em text box 
def on_clickA(event):
    if caixa_textoA.get() == "Digite o valor A":
        caixa_textoA.delete(0, "end") # remove o texto explicativo
def on_clickB(event):
    if caixa_textoB.get() == "Digite o valor B":
        caixa_textoB.delete(0, "end") # remove o texto explicativo

#Fazendo o botão de soma funcionar
def on_click_soma():
    try:
        valor_a = int(caixa_textoA.get())
        valor_b = int(caixa_textoB.get())
        rotulo_soma["text"] = f"O valor da soma entre os números recebidos é {valor_a + valor_b}"
        
    except ValueError:
        
        got_an_error = tk.Label(window,text="Por favor insira apenas numeros...")
        got_an_error.config(bg="red")
        got_an_error.pack(side="bottom")
        

#Criando uma janela
window = tk.Tk()

#Definindo titulo da janela
window.title("Tkinter teste")

#Definindo tamanho da tela
window.geometry("400x300")

#Adiciona um texto na tela
rotulo = tk.Label(window,text="Testando Tkinter!!")
rotulo.pack()

rotulo = tk.Label(window,text="Fazendo um aplicativo de soma")
rotulo.pack(pady=10)

caixa_textoA = tk.Entry(window, width=30,)
caixa_textoA.insert(0, "Digite o valor A")
caixa_textoA.bind("<FocusIn>", on_clickA)
caixa_textoA.pack(pady=10)

valor_A = caixa_textoA.get() #Pegando valores inseridos na caixa de texto

caixa_textoB = tk.Entry(window, width=30)
caixa_textoB.insert(0, "Digite o valor B")
caixa_textoB.bind("<FocusIn>", on_clickB)
caixa_textoB.pack(pady=10)

valor_B = caixa_textoA.get() #Pegando valores inseridos na caixa de texto

botao = tk.Button(window, text="Realizar soma", command=on_click_soma)
botao.pack(pady=10)

#Mostrando valor da soma

rotulo_soma = tk.Label(window,text="")
rotulo_soma.pack(pady=10)

#Mantem a janela aberta
window.mainloop()