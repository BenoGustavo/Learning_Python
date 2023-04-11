from random import randint
import sys

for i in range(100):

    cpf = ''
    for i in range(9):
        if i == 3 or i == 6:
            cpf += '.'

        cpf += str(randint(0,9))

        if i == 8:
            cpf += '-'

    ultimos_nove_digitos = cpf[:-1]

    contador = 10
    Primeiro_digito = 0

    for numeros in ultimos_nove_digitos:
        if numeros == '.':
            continue

        Primeiro_digito += int(numeros) * contador
        contador=contador-1

    Primeiro_digito = ((Primeiro_digito*10)%11)

    if Primeiro_digito > 9:
        Primeiro_digito = 0
    else:
        Primeiro_digito = Primeiro_digito

    #Calculo do segundo digito do CPF

    #Passam a ser dez digitos por conta do valor acrescentado

    ultimos_dez_digitos = ultimos_nove_digitos + str(Primeiro_digito)

    contador = 11
    Segundo_digito = 0

    for numeros in ultimos_dez_digitos:
        if numeros == '.':
            continue

        Segundo_digito += int(numeros) * contador
        contador=contador-1

    Segundo_digito = ((Segundo_digito*10)%11)

    if Segundo_digito > 9:
        Segundo_digito = 0
    else:
        Segundo_digito = Segundo_digito

    cpf = cpf + str(Primeiro_digito) + str(Segundo_digito)

    CPF_GERADO = f'{ultimos_nove_digitos}-{Primeiro_digito}{Segundo_digito}'

    if cpf == CPF_GERADO:
        print(f"\nO CPF [{cpf}]")
    else:
        print(f"\nO CPF [{cpf}] enviado é invalido\n")