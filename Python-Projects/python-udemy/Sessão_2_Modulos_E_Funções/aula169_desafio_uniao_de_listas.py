# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

def cidades_capital(a,b):
    if a > b:
        return list(zip(a,b))
    else:
        return list(zip(b,a))

Cidades = ['BA', 'SP', 'MG', 'RJ']
Capitais = ['Salvador', 'Ubatuba', 'Belo Horizonte']

print(cidades_capital(Capitais,Cidades))