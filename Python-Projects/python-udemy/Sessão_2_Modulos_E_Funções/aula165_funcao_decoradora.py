def decoradora(funcao):
    def wrap(*args): #Função interna que atrasa a execução de outras funções
        print("Antes de executar a função...")
        rodando_a_funcao = funcao(*args)
        print("Depois de executar a função...")
        return rodando_a_funcao
    return wrap

@decoradora
def soma(*args):
    soma_dos_valores = 0
    
    for numero in args:
        soma_dos_valores += numero
    return soma_dos_valores

soma_de_dois_numeros = soma(5,5)

print(soma_de_dois_numeros)