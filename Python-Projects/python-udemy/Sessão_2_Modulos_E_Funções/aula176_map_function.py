from functools import partial

def print_iteravel(lista):
    print(*list(lista), sep='\n')

def aumentar_porcentagem(valor, porcentagem):
    return round(valor * porcentagem, 2)

def muda_preco_de_produtos(produto):
    return {**produto,'preco': partial(aumentar_porcentagem,porcentagem=1.1)(produto['preco'])}

lista = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

novos_produtos = list(map(muda_preco_de_produtos,lista))

print_iteravel(novos_produtos)

#Mapping comm lambda

print(list(map(lambda x: x * 2 ,)))