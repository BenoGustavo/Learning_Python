def soma(x,y):
    return x+y

def multiplica(x,y):
    return x*y

def executa(funcao, x):
    def closure(y):
        return funcao(x,y)
    return closure

soma_com_cinco = executa(soma, 5)
multiplica_por_dez = executa(multiplica, 10)

print(soma_com_cinco(10), multiplica_por_dez(10))