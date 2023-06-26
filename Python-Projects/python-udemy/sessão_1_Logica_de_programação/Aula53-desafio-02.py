"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

horas = input("Insira as horas: ")

try:
    manha = int(horas) > 0 and int(horas) <= 11
    tarde = int(horas) >= 12 and int(horas) <= 17
    noite = int(horas) >= 18 and int(horas) <= 23
    inexistente = int(horas) >=24

    if manha:
        print("Bom Dia!!")

    if tarde:
        print("Boa Tarde!!")

    if noite:
        print("Boa noite!!")
        
    if inexistente:
        print("O número digitado é maior ou igual a 24")
        
except:
    print("O valor inserido não é um número")

