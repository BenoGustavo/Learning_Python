#Funções recursivas ficam em loop, quase igual a um while ou for, tentando chegar ao final desejado
#Normalmente apenas são utilizadas em programação funcional, pois é basicamente um loop

import sys

sys.setrecursionlimit(1004) #Evita stackoverflow no seu codigo, porém n é recomendavel pois pode travar sua maquina

def recursiva(inicio=0,fim=15):
    if inicio >= fim:
        return fim
    
    inicio += 1

    return recursiva(inicio,fim)

print(recursiva())

#Exemplo pratico fatorial


def facto_func(num=1):

    if num <= 1:
        return 1
        
    return num * facto_func(num - 1)

print(facto_func(5))