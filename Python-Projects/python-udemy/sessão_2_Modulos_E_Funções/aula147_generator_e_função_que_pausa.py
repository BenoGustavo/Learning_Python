

def generator(n=0, maximum=10):

    while True: #LOOP INFINITO
        
        yield n #PAUSA A FUNÇÃO E RETORNA CERTO VALOR, TRANSFORMANDO O MESMO EM UM ITERAVEL
        n += 1

        if n >= maximum: #PARA A FUNÇÃO E RETORNA NADA
            return
        
gen = generator(n=10,maximum=100) #DA O VALOR A UMA VARIAVEL E TAMBÉM O VALOR MAXIMO E O MINIMO

for n in gen:
    print(n) #FAZ A ITERAÇÃO DOS VALORES