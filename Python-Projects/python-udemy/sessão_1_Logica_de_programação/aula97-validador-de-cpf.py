#Calculo do primeiro digito do CPF
import sys

print("Insira o CPF com pontos e traços ou apenas o traço")
cpf =input("Insira seu CPF no formato (*********-**): ")

if not '-' in cpf:
    print("\n\nPor favor, insira o CPF conforme o modelo (Sem pontos e com traço)")
    sys.exit()

if not '.' in cpf:
    ponto = 1
    cpf_com_pontos = ''
    for number in cpf:
        cpf_com_pontos=cpf_com_pontos + number
        if ponto == 3 or ponto == 6:
            cpf_com_pontos = cpf_com_pontos+'.'
        ponto += 1

ultimos_nove_digitos = cpf[:-3]
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

CPF_GERADO = f'{ultimos_nove_digitos}-{Primeiro_digito}{Segundo_digito}'

if cpf == CPF_GERADO:
    print(f"\nO CPF [{cpf}] enviado é válido\n")
else:
    print(f"\nO CPF [{cpf}] enviado é invalido\n")