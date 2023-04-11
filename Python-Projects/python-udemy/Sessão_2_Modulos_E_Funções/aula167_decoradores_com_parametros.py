def parametros_do_decorador(a=None, b=None, c=None):
    def decorador(funcao):
        
        def wrap(*args):

            print("Antes de executar a função...")
            executando_a_funcao = funcao(*args, a, b, c)
            print("Depois de executar a função")

            return executando_a_funcao
        return wrap
    return decorador


@parametros_do_decorador(1,1,1)
def soma(*args):
    soma_dos_valores = 0

    for numero in args:
        soma_dos_valores += numero

    return soma_dos_valores


soma_dos_valores = soma(5, 5)

print(soma_dos_valores)
