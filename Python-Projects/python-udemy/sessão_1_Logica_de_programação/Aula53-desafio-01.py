"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

numero_inteiro = input("Digite um número inteiro: ")

try:
    par_ou_impar = int(numero_inteiro)% 2 == 0

    if par_ou_impar:
        print("Seu número é par")
    else:
        print("Seu número é impar")

except:
    print('Isso não é um número inteiro')