from random import shuffle
from os import system
from time import sleep

def adicionar_filme(filme, lista=None):
    if lista is None:
        lista = []
    
    lista.append(filme)
    return lista

def aleatorizar(lista=None):
    if lista is None:
        raise ValueError("Adicione primeiro um filme a lista...")

    shuffle(lista)

    aleatorizado = lista.pop()

    return aleatorizado

def mostrar_filmes(lista=None):
    if lista is None or lista is "":
        raise ValueError("Adicione primeiro um filme a lista...")
    
    for count,item in enumerate(lista):
        print(f"{count} - {str(item).title()}")

        return

filmes = None

while True:
    system("cls")
    escolha = input("Aleatorizador de filmes\nInsira o que deseja:\n\n[Adicionar] filmes[1]\n[Aleatorizar] filmes[2]\n[Remover] filme[3]\n[Limpar] lista[4]\n")

    if escolha == '1':
        system("cls")
        print("Aleatorizador de filmes\n\n")
        print("Filmes na lista:")

        try:
            mostrar_filmes(filmes)
        except ValueError as error:
            print(f"{error}\n")
            
            selected = input("Aperte qualquer tecla para retornar...")
            continue
       
        nome_filme = input("\nInsira o nome do filme que deseja adicionar: ")

        filmes = adicionar_filme(nome_filme)
        
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
        
        print(f"O filme escolhido foi {selected}\n\n")
        
        selected = input("Aperte qualquer tecla para retornar...")
        continue

    elif escolha == '3':
        system("cls")
        print("Aleatorizador de filmes\n\n")

        try:
            mostrar_filmes(filmes)
        except ValueError as error:
            print(f"{error}\n")
            
            selected = input("Aperte qualquer tecla para retornar...")
            continue
        
        delete = input("Insira o indice do filme a ser deletado: ")

        try:
            filmes.remove(int(delete))
        except ValueError:
            print("Insira um indice valido...\n")

            selected = input("Aperte qualquer tecla para retornar...")
            continue

        nome_filme = input("Filmes adicionado com sucesso\n\n Aperte qualquer tecla para retornar...")
        continue

    elif escolha == '4':
        system("cls")
        print("Aleatorizador de filmes\n\n")

        try:
            mostrar_filmes(filmes)
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

        else:
            print("Comando invalido")
            print("Retornando...")
            sleep(2)
            continue