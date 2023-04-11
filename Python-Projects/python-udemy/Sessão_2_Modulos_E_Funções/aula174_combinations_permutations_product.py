from time import sleep
import os
from itertools import combinations,permutations,product

#Função que facilita a vizualização de listas e iteraveis

def print_iteravel(lista):
    print(*list(lista), sep='\n')

pessoas = ['João','Maria','José','Luiz','Guilherme']

#Lista de listas

camisas = [
    ['preta','branca','azul'],
    ['pp','p','m','g','gg'],
    ['male','female','unisex'],
]

print('Exemplo de uso do combinations (Grupos unicos, não repetindo itens)\n')

print_iteravel(combinations(pessoas,2)) #(lista, tamanho do grupo)

sleep(2.5)
os.system('cls')

print('Exemplo de uso do permutations (Todas as possibilidades de combinações)\n')

print_iteravel(permutations(pessoas,2))

sleep(2.5)
os.system('cls')

print('Exemplo de uso do product (em formato de produtos)\n')

print_iteravel(product(*camisas))