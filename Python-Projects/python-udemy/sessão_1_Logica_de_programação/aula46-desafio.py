name = input("Insira seu nome: ")
age = input("Insira sua idade: ")

if not name or not age:
    print("Você não inseriu todas as informações necessarias.")
else:
    nameChar = len(name)

    print(f"Seu nome é {name}")
    print(f"Seu nome invertido fica {name[::-1]}")
    print(f"Seu nome tem {nameChar} letras")

    if ' ' in name:
        print("Seu nome tem espaços")
    else:
        print("Seu nome não tem espaços")

    print(f"A primeira letra do seu nome é {name[0]}")
    print(f"A ultima letra do seu nome é {name[nameChar-1]}")