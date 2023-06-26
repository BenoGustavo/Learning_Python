'''
A função def permite que você crie partes de codigos que possam 
ser facilmente reutilizavel.
'''

#Exemplo print()

def imprimir_na_tela(a = 'Nada inserido',b = 'Nada inserido',c = 'Nada inserido'):
    print(f"Imprimindo na tela o que você escrever em [a]: [{a}]")
    print(f"Imprimindo na tela o que você escrever em [b]: [{b}]")
    print(f"Imprimindo na tela o que você escrever em [c]: [{c}]")

#Exemplo Soma()

def soma(a ,b , c=None):
    if c is not None:
        print("Somei A + B + C para vc: ")
        return(a+b+c)
    else:
        print("Somei A + B para vc: ")
        return(a+b)

#utilizando as def

print(soma(5,5))
print(soma(5,5,5))


print('\n\n')
imprimir_na_tela()
print('\n\n')
imprimir_na_tela('foda fi','to botando coisa','Aqui')

