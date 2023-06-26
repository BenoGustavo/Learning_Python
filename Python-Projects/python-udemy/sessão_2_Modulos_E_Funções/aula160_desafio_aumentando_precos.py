# copy, sorted, produtos.sort

# Exercícios


# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)

from copy import deepcopy as dc

contador = 0

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

print("Produtos Originais")
print(*produtos, sep="\n")
print("\n\n")

novos_produtos = dc(produtos)

for lista in produtos:
    porcentagem = lista['preco'] * 0.10
    novo_valor = lista['preco'] + porcentagem

    lista['preco'] = round(novo_valor, 2)
    
    novos_produtos[contador].update({"preco": lista['preco']})

    contador += 1

print("Produtos 10%")
print(*novos_produtos, sep="\n")
print("\n\n")

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

produtos_ordenados_por_nome = dc(novos_produtos)

produtos_ordenados_por_nome = sorted(produtos_ordenados_por_nome, key=lambda d:d['nome'])

print("Produtos Ordenados por nome")
print(*produtos_ordenados_por_nome, sep="\n")
print("\n\n")

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

produtos_ordenados_por_preco = dc(novos_produtos)

print("Produtos Ordenados por preço")
produtos_ordenados_por_preco = sorted(produtos_ordenados_por_nome, key=lambda d:d['preco'])

print(*produtos_ordenados_por_preco, sep="\n")
print("\n\n")