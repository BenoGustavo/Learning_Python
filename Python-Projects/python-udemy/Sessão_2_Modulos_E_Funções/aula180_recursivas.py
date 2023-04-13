#Funções recursivas ficam em loop, quase igual a um while ou for, tentando chegar ao final desejado

def recursiva(inicio=0,fim=15):
    if inicio >= fim:
        return fim
    
    inicio += 1

    return recursiva(inicio,fim)

print(recursiva())