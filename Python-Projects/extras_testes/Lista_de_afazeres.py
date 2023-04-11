import os
from time import sleep

lista = []
conclusao = 0

while True:
    cont = 0

    os.system("cls")

    try:
        print(f"Barra de progresso: {conclusao} / {len(lista)} ou {(conclusao/len(lista)) * 100}%\n")
    except ZeroDivisionError:
        print(f"Barra de progresso: {conclusao} / {len(lista)} ou 0%\n")

    for item in lista: 
        print(item,sep=' || ',end="\n")

    option = input("1 - Adicionar uma tarefa || 2 - Marcar uma tarefa como concluida \n3 - Atualizar uma tarefa || 4 - Deletar uma tarefa \nO que você gostaria de fazer? ")

    if option == '1' or option.lower() == 'adicionar' or option.lower() == 'adicionar uma tarefa':
        adicionar_lista = input("Escreva o que você deseja adicionar à lista: ")
        
        lista.append(adicionar_lista)
        print("Adicionado com sucesso")
        sleep(2)
        os.system("cls")
        continue

    if option == '2' or option.lower() == 'marcar uma tarefa como concluida' or option.lower() == 'concluida':
        if len(lista) == 0:
            print("Você não tem tarefas para marcar como concluida...")
            sleep(2)
            os.system("cls")
            break

        os.system("cls")

        for item in lista:
            print(f"{cont} - {item}")
            cont += 1
        
        while True:
            try:
                concluida = int(input("\nQual das tarefas você deseja marcar como concluida?(num) "))
                
                if concluida >= len(lista):
                    print("O valor digitado é invalido, retornando")
                        
                    sleep(2)
                    os.system("cls")
                    continue
                
                log = lista[concluida] + ' - (Concluida)'

                lista[concluida] = log

                print("\nLista atualizada com sucesso...")
                conclusao += 1
                sleep(2)
                os.system("cls")

                break
            except ValueError:
                print("\n O comando deve ser um número...")

    if option == '3' or option.lower() == 'atualizar uma tarefa' or option.lower() == 'atualizar':
        if len(lista) == 0:
            print("Você não tem tarefas para atualizar...")
            sleep(2)
            os.system("cls")
            continue
        
        while True:
            os.system("cls")

            for item in lista:
                print(f"{cont} - {item}")
                cont += 1

            try:
                atualizar = int(input('Insira o indice da tarefa a ser atualizada: '))

            except ValueError:
                print("O valor digitado deve ser um indice, tente novamente...")

            if atualizar >= len(lista):
                print("Indice não encontrado, retornando")        
                sleep(2)
                os.system("cls")

                continue

            print('\n' + lista[atualizar])
            atualizar_txt = input("Insira a substituição: ")

            esta_concluida = lista[atualizar][-11::] == '(Concluida)'

            lista[atualizar] = atualizar_txt

            if esta_concluida:
                lista[atualizar] = lista[atualizar] + ' - (Concluida)'

            print("\nAtualização realizada com sucesso, retornando...")

            sleep(2)
            break
    
    if option == '4' or option.lower() == 'deletar uma tarefa' or option.lower() == 'deletar':
        if len(lista) == 0:
            print("Você não tem tarefas para deletar...")
            sleep(2)
            os.system("cls")
            continue

        while True:
            os.system("cls")

            for item in lista:
                print(f"{cont} - {item}")
                cont += 1

            try:
                deletar = int(input("Insira o indice da tarefa a ser deletada: "))

            except ValueError:
                print("Por favor, insira um indice valido...")

            if deletar >= len(lista):
                print("Indice não encontrado, retornando")        
                sleep(2)
                os.system("cls")

                continue

            lista.remove(lista[deletar])

            print("Item deletado com sucesso, retornando...")
            sleep(2)
            os.system('cls')
            break
    
    else:
        print("\nPor favor digite uma opção valida, retornando.")
