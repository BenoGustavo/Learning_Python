#Utilizando filtros dentro de dados em uma lista de dicionarios

def print_iter(lista):
    print(*lista, sep='\n')


produtos = [
    {'nome':'produto1','preco':10.00},
    {'nome':'produto2','preco':100.00},
    {'nome':'produto3','preco':22.32},
    {'nome':'produto4','preco':10.11},
    {'nome':'produto5','preco':69.90}
]

novo_produto = filter(lambda x: x['preco'] > 10, produtos)

print_iter(novo_produto)