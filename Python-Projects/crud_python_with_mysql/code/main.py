import crud_clinica,crud_funcionario,crud_hospital,crud_paciente
from os import system
from time import sleep

while True:
    system("cls") #Limpando o terminal

    print("Sistema de prontuarios\n")
    print("Quais dados deseja manipular?")
    print("(1) - Funcionario")
    print("(2) - Paciente")
    print("(3) - Hospital")
    print("(4) - Clinica")
    option = int(input("(5) - Sair"))

    if option == 1:
        print("Insira o que deseja: Funcionario")
        print("(1) - Cadastrar funcionario")
        print("(2) - Ler funcionario")
        print("(3) - Atualizar funcionario")
        print("(4) - Deletar funcionario [Não funciona]")
        option_interno = int(input("(5) - Retornar"))

        if option_interno == 1:
            pass

        if option_interno == 2:
            pass

        if option_interno == 3:
            pass

        if option_interno == 4:
            pass

        else:
            print("Opção desconhecida...")
            sleep(2)
            continue

    if option == 2:
        print("Insira o que deseja: Paciente")
        print("(1) - Cadastrar paciente")
        print("(2) - Ler paciente")
        print("(3) - Atualizar paciente")
        print("(4) - Deletar paciente [Não funciona]")
        option_interno = int(input("(5) - Retornar"))

        if option_interno == 1:
            pass

        if option_interno == 2:
            pass

        if option_interno == 3:
            pass

        if option_interno == 4:
            pass

        else:
            print("Opção desconhecida...")
            sleep(2)
            continue

    if option == 3:
        print("Insira o que deseja: Hospital")
        print("(1) - Cadastrar hospital")
        print("(2) - Ler hospital")
        print("(3) - Atualizar hospital")
        print("(4) - Deletar hospital [Não funciona]")
        option = int(input("(5) - Retornar"))

        if option_interno == 1:
            pass

        if option_interno == 2:
            pass

        if option_interno == 3:
            pass

        if option_interno == 4:
            pass

        else:
            print("Opção desconhecida...")
            sleep(2)
            continue

    if option == 4:
        print("Insira o que deseja: Clinica")
        print("(1) - Cadastrar clinica")
        print("(2) - Ler clinica")
        print("(3) - Atualizar clinica")
        print("(4) - Deletar clinica [Não funciona]")
        option = int(input("(5) - Retornar"))

        if option_interno == 1:
            pass

        if option_interno == 2:
            pass

        if option_interno == 3:
            pass

        if option_interno == 4:
            pass

        else:
            print("Opção desconhecida...")
            sleep(2)
            continue

    if option == 5:
        exit(0)

    else:
        sleep(2)
        print("Opção desconhecida...")
        continue