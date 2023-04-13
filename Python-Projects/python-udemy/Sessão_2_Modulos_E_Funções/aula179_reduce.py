#Funcao reduce que serve para retornar um valor de uma lista

from functools import reduce

produtos = [
    {'nome':'produto1','preco':10.00},
    {'nome':'produto2','preco':100.00},
    {'nome':'produto3','preco':22.32},
    {'nome':'produto4','preco':10.11},
    {'nome':'produto5','preco':69.90}
]

#Finalmente entendi lambda || ao inves da lambda pode ser usado

#def somando(acumulador,produto):
#    return acumulador + produto

soma_dos_precos = reduce(lambda acumulador,produto:acumulador + produto['preco'] ,produtos,0 )

print(soma_dos_precos)