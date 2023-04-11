"""
Iterando strings com while
"""

while True:

    print("\nVocê pode sair digitando 'Sair'")
    nome = input("Insira seu nome: ")
    len_nome = len(nome)

    nome.capitalize

    i=0
    nova_string = ''

    if nome == 'Sair':
        break
    
    while len_nome > i:
        nova_string += nome[i]

        print(f"A {i} do seu nome é: {nome[i]}")
        print(f'Ou seja {nova_string}')

        i +=1