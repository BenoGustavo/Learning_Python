"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
name = input("Escreva seu primeiro nome: ")

try:
    len_name = len(name)

    nome_zerado = len_name < 1
    nome_curto = len_name >= 1 and len_name <= 4
    nome_normal = len_name >= 5 and len_name <= 6
    nome_grande = len_name > 6

    if nome_zerado:
        print("Seu nome tem ZERO letras")

    if nome_curto:
        print(f"Seu nome {name} pode ser considerado curto")
    if nome_normal:
        print(f"Seu nome {name} pode ser considerado mediano")
    if nome_grande:
        print(f"Seu nome {name} pode ser considerado grande")
except:
    print("Isso não é um nome")