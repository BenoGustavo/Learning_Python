import mysql.connector

from crud_funcionario import create_funcionario,read_funcionario,update_funcionario,delete_funcionario, show_all_id_from_table, show_all_name_from_table

from os import system
from time import sleep

while True:
    name_funcionario = show_all_name_from_table("Funcionario")
    id_funcionario = show_all_id_from_table("Funcionario")

    dados_funcionario = zip(id_funcionario,name_funcionario)


    system("cls") #Limpando o terminal

    print("Sistema de prontuarios\n")
    print("Quais dados deseja manipular?")
    print("(1) - Funcionario")
    print("(2) - Paciente")
    print("(3) - Hospital")
    print("(4) - Clinica")
    option = int(input("(5) - Sair\n"))

    if option == 1:
        system("cls") #Limpando o terminal
        print("Insira o que deseja: Funcionario")
        print("(1) - Cadastrar funcionario")
        print("(2) - Ler funcionario")
        print("(3) - Atualizar funcionario")
        print("(4) - Deletar funcionario ")
        option_interno = int(input("(5) - Retornar\n"))

        if option_interno == 1: #Cadastrar funcionario

            system("cls") #Limpando o terminal
            cpf = input("Insira o CPF do funcionario (Apenas números): ")
            nome = input("Insira o nome do funcionario: ")
            email = input("Insira o email do funcionario: ")
            telefone = input("Insira o telefone do funcionario: ")
            funcao = input("Insira a função do funcionario: ")
            logradouro = input("Insira o logradouro do funcionario: ")
            bairro = input("Insira o bairro do funcionario: ")
            numero_casa = input("Insira o numero domestico do funcionario: ")
            cep = input("Insira o CEP do funcionario (Apenas numeros): ")
            definitivo = input("Deseja mesmo cadastrar este funcionario? (y) or (n)")

            if definitivo.lower() == 'y':
                try:
                    create_funcionario(cpf,nome,email,telefone,logradouro,funcao,cep,numero_casa,bairro)

                    print("\nFuncionario cadastrado com sucesso...")
                    sleep(3)
                    continue

                except Exception as error:
                    print("O cadastro falhou...")
                    print(error)
                    sleep(1)
                    continue

            if definitivo.lower() == 'n':
                continue

        if option_interno == 2: #Ler funcionario
            system("cls") #Limpando o terminal

            for dado in dados_funcionario:
                print(str(dado).replace("(","").replace(")","").replace(",",""))
            print("")

            id_funcionario = input("Insira o ID do funcionario: ")

            try:
                print(read_funcionario(id_funcionario))
            
            except TypeError:
                print("\nID não encontrada retornando...")
                sleep(1.5)
                continue

            press = input("\nAperte qualquer tecla para voltar...")
            continue

        if option_interno == 3:
            system("cls") #Limpando o terminal

            for dado in dados_funcionario:
                print(str(dado).replace("(","").replace(")","").replace(",",""))
            print("")

            id_funcionario = input("ID do funcionario: ")
            cpf = input("CPF funcionario: ")
            nome = input("Nome do funcionario: ")
            email = input("Email do funcionario: ")
            telefone = input("Telefone do funcionario: ")
            logradouro = input("Logradouro do funcionario: ")
            funcao =  input("Funcao do funcionario: ")
            cep = input("CEP do funcionario: ")
            numero = input("Numero da residencia do funcionario: ")
            bairro = input("Bairro do funcionario: ")
            
            update_funcionario(id_funcionario,cpf,nome,email,telefone,logradouro,funcao,cep,numero,bairro)

            print("\nFuncionario atualizado com sucesso...")
            sleep(1)
            continue

        if option_interno == 4:
            system("cls") #Limpando o terminal

            for dado in dados_funcionario:
                print(str(dado).replace("(","").replace(")","").replace(",",""))
            print("")
            
            id_funcionario = input("Insira o ID do funcionario: ")
            
            try:
                delete_funcionario(id_funcionario)
                print("Funcionario deletado com sucesso...")
                sleep(1.5)
                continue
            except TypeError:
                
                print("Falha ao deletar o usuario")
                sleep(2)
                continue

        else:
            print("Opção desconhecida...")
            sleep(2)
            continue

    if option == 2:
        system("cls") #Limpando o terminal
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
        system("cls") #Limpando o terminal
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

        if option_interno == 5: #Retornar
            continue

        else:
            print("Opção desconhecida...")
            sleep(2)
            continue

    if option == 4:
        system("cls") #Limpando o terminal
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