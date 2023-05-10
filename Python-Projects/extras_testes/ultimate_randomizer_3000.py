from random import shuffle
from os import system
from time import sleep

def adicionar_filme(filme, lista=None):
    if lista is None:
        lista = []
    
    lista.append(filme)
    return lista

def aleatorizar(lista=None):
    if lista is None or not lista:
        raise ValueError("Adicione primeiro um filme a lista...")

    shuffle(lista)

    aleatorizado = lista.pop()

    return aleatorizado

def mostrar_filmes(lista=None):
    if lista is None or not lista:
        raise ValueError("Adicione primeiro um filme a lista...")
    

    count = 0
    for item in lista:
        print(f"{count} - {str(item).title()}")
        
        count += 1

    return

anterior = ""
filmes = []

while True:
    system("cls")
    print("Aleatorizador de filmes\nInsira o que deseja:\n\nAdicionar filmes[1]\nAleatorizar filmes[2]\nRemover filme[3]\nLimpar lista[4]")
    
    if anterior != "":
        print("Adicionar ultimo deletado a lista [5]\n")

    escolha = input()

    if escolha == '1':
        system("cls")
        print("Aleatorizador de filmes\n\n")
       
        nome_filme = input("\nInsira o nome do filme que deseja adicionar: ")

        filmes = adicionar_filme(nome_filme,list(filmes))
        
        nome_filme = input("Filmes adicionado com sucesso\n\n Aperte qualquer tecla para retornar...")
        continue

    elif escolha == '2':
        system("cls")
        print("Aleatorizador de filmes\n\n")
        print("Filmes na lista:")
        
        try:
            mostrar_filmes(filmes)
        except ValueError as error:
            print(f"{error}\n")
            
            selected = input("Aperte qualquer tecla para retornar...")
            continue

        try:
            selected = aleatorizar(filmes)
        except ValueError as error:
            print(f"{error}\n")
        
            selected = input("Aperte qualquer tecla para retornar...")
            continue
        
        print(f"\nO filme escolhido foi {selected}\n\n")
        
        selected = input("Aperte qualquer tecla para retornar...")
        continue

    elif escolha == '3':
        system("cls")
        print("Aleatorizador de filmes\n\n")

        try:
            mostrar_filmes(list(filmes))
        except ValueError as error:
            print(f"{error}\n")
            
            selected = input("Aperte qualquer tecla para retornar...")
            continue
        
        delete = input("\nInsira o indice do filme a ser deletado: ")

        try:
            anterior = filmes.pop(int(delete))
        except ValueError:
            print("Insira um indice valido...\n")

            selected = input("Aperte qualquer tecla para retornar...")
            continue

        nome_filme = input("Filmes deletado com sucesso\n\n Aperte qualquer tecla para retornar...")
        continue

    elif escolha == '4':
        system("cls")
        print("Aleatorizador de filmes\n\n")

        try:
            mostrar_filmes(list(filmes))
        except ValueError as error:
            print(f"{error}\n")
            
            selected = input("Aperte qualquer tecla para retornar...")
            continue
        
        deseja_mesmo_deletar = input("Deseja mesmo deletar toda sua lista atual? [S] or [N]: ")

        if deseja_mesmo_deletar.upper() == "S":
            filmes.clear()
            
            nome_filme = input("Filmes deletado com sucesso\n\n Aperte qualquer tecla para retornar...")
            continue

        elif deseja_mesmo_deletar.upper() == "N":
            continue

    elif escolha == "5":
        system("cls")
        print("Aleatorizador de filmes\n\n")
        print("Filmes na lista:")

        try:
            mostrar_filmes(filmes)
        except ValueError as error:
            print(f"Nenhum filme na lista...")

        selected = input(f"\nDeseja retornar o filmes {anterior} para a lista? [S] or [N] ")

        if selected.upper() == 'S':
            filmes.append(anterior)
            
            nome_filme = input("Filmes adicionado com sucesso\n\n Aperte qualquer tecla para retornar...")
            continue
        
        elif selected.upper() == 'N':
            continue

        else:
            print("Comando invalido")
            print("Retornando...")
            sleep(2)
            continue