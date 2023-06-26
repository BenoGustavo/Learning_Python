from os import system

lista_de_compras = []
comandos_validos = 'adddelclearsair'

while True:

    acao = input("Comandos - Lista de compras\n\nAdicionar[add] - Deletar [del]\nLimpar lista[Clear] - Sair para [sair]: ")

    try:
        if acao not in comandos_validos:
            system("cls")
            print("\nInsira um comando valido\n")
            continue

        if acao == 'add':
            system("cls")
            for indice, item in enumerate(lista_de_compras):
                print(f"Indice: {indice} || Item: {item}")
            lista_de_compras.append(input("\nInsira o item que deseja adicionar a lista: "))
            continue

        if acao == 'del' and len(lista_de_compras) > 0:
            system("cls")
            for indice, item in enumerate(lista_de_compras):
                print(f"Indice: {indice} || Item: {item}")
            lista_de_compras.remove(input("\nInsira o indice do item que deseja remover a lista: "))
            continue

        if acao == 'clear' and len(lista_de_compras) > 0:
            system("cls")
            lista_de_compras.clear()
            continue

        if acao == 'sair':
            break

        if len(lista_de_compras) == 0:
            print("\nPrimeiro é necessario adicionar algo a sua lista...")
            continue
    except:
        print("\n\nInsira um valor dentro dos indices existentes...\n")