def multiplicacao(*args):
    total = 1
    for numeros in args:
        total *= numeros
    return total

def encontre_impar_ou_par(*args):
    impar_ou_par = ''
    for numeros in args:
        if numeros % 2 == 0:
            impar_ou_par += f'O número {numeros} é par\n'
        else:
            impar_ou_par += f'O número {numeros} é ímpar\n'
    return impar_ou_par

testando_uma_nova_funcao = encontre_impar_ou_par(1,2,3,4,5,6,7,8,9)

print(testando_uma_nova_funcao)

testando_uma_nova_funcao = multiplicacao(5,5,5)

print(testando_uma_nova_funcao)
    