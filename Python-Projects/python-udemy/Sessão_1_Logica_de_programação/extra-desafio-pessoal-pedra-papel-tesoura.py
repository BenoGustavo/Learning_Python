"""
Machine plays: 1 - Rock, 2 - Paper, 3 - Scissors
"""

while True:
    from random import randint

    #Jogada Humana

    possiveis_jogadas = ('PedraPapelTesoura')

    player = input("\n\nFaça sua jogada Pedra, Papel Ou Tesoura: ")
    player = player.capitalize()

    if player not in possiveis_jogadas:
        print(f"A jogada {player} não é valida, por favor insira uma que seja valida")
        break

    #Jogada Maquina
    jogada_maquina = randint(1,3)

    #Inserindo a jogada da Maquina
    if jogada_maquina == 1:
        jogada_maquina = "Pedra"

    elif jogada_maquina == 2:
        jogada_maquina = "Papel"

    elif jogada_maquina == 3:
        jogada_maquina = "Tesoura"

    #Definindo Vencedor
    if player == "Pedra" and jogada_maquina != "Pedra":
        if jogada_maquina == "Tesoura":
            print(f"\nJogador ganhou || J1 {player} x M1 {jogada_maquina}")
        elif jogada_maquina == "Papel":
            print(f"\nMaquina ganhou || J1 {player} x M1 {jogada_maquina}")

    elif player == "Papel" and jogada_maquina != "Papel" :
        if jogada_maquina == "Tesoura":
            print(f"\nMaquina ganhou || J1 {player} x M1 {jogada_maquina}")
        elif jogada_maquina == "Pedra":
            print(f"\nJogador ganhou || J1 {player} x M1 {jogada_maquina}")

    elif player == "Tesoura" and jogada_maquina != "Tesoura":
        if jogada_maquina == "Papel":
            print(f"\nJogador ganhou || J1 {player} x M1 {jogada_maquina}")
        elif jogada_maquina == "Pedra":
            print(f"\nMaquina ganhou || J1 {player} x M1 {jogada_maquina}") 

    #Definindo se foi empate ou não

    elif player == jogada_maquina:
        print(f"\nEmpate || J1 {player} x M1 {jogada_maquina}")

    sair = input(f"\n\nDeseja sair? [s]im, ou qualquer tecla para continuar: ")

    if sair.lower() == 's':
        break