"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.
Exemplo:
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]
=================== resultado
lista_soma  = [2, 4, 6, 8]
"""

def soma_de_listas(lista1, lista2):
    soma_das_listas = []
    max = min(len(lista1), len(lista2))

    for i in range(max):
        soma_das_listas.append(lista1[i] + lista2[i])

    return soma_das_listas


valores_a = [1, 2, 3, 4, 5, 6, 7]
valores_b = [1, 2, 3, 4]

print(soma_de_listas(valores_a,valores_b))
