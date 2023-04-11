'''
Args permite que você use uma quantidade indefinida de coisas dentro de uma função
'''

def somar(*args):
    total = 0
    for numero in args:
        total += numero
    return total 

teste_soma_funcao = somar(2,2,2)

print(teste_soma_funcao)
