import tkinter as tk
from tkinter import messagebox

class JogoDaVelha:
    def __init__(self):
        self.jogador_atual = "X"
        self.tabuleiro = [["" for _ in range(3)] for _ in range(3)]
        
        self.janela = tk.Tk()
        self.janela.title("Jogo da Velha")
        
        self.botoes = [[None for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.botoes[i][j] = tk.Button(self.janela, text="", width=10, height=5,
                                             command=lambda row=i, col=j: self.jogada(row, col))
                self.botoes[i][j].grid(row=i, column=j)
        
        self.botao_reiniciar = tk.Button(self.janela, text="Reiniciar", width=10, command=self.reiniciar)
        self.botao_reiniciar.grid(row=3, column=0, columnspan=3)
        
    def jogada(self, row, col):
        if self.tabuleiro[row][col] == "":
            self.tabuleiro[row][col] = self.jogador_atual
            self.botoes[row][col].config(text=self.jogador_atual)
            if self.verificar_vitoria():
                messagebox.showinfo("Fim de jogo", f"O jogador {self.jogador_atual} venceu!")
                self.reiniciar()
            elif self.verificar_empate():
                messagebox.showinfo("Fim de jogo", "Empate!")
                self.reiniciar()
            else:
                self.jogador_atual = "O" if self.jogador_atual == "X" else "X"
        
    def verificar_vitoria(self):
        for i in range(3):
            if self.tabuleiro[i][0] == self.tabuleiro[i][1] == self.tabuleiro[i][2] != "":
                return True
            if self.tabuleiro[0][i] == self.tabuleiro[1][i] == self.tabuleiro[2][i] != "":
                return True
        if self.tabuleiro[0][0] == self.tabuleiro[1][1] == self.tabuleiro[2][2] != "":
            return True
        if self.tabuleiro[0][2] == self.tabuleiro[1][1] == self.tabuleiro[2][0] != "":
            return True
        return False
    
    def verificar_empate(self):
        for row in self.tabuleiro:
            if "" in row:
                return False
        return True
    
    def reiniciar(self):
        self.jogador_atual = "X"
        self.tabuleiro = [["" for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.botoes[i][j].config(text="")
    
    def iniciar(self):
        self.janela.mainloop()

jogo = JogoDaVelha()
jogo.iniciar()