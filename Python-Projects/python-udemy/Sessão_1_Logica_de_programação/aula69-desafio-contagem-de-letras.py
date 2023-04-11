frase = input('Escreva a frase que deseja analisar: ')

i=0
letra_atual = ''
maior_aparecido = 0
contagem_atual = 0
indice_do_mais_aparecido = 0
repetido = 0

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i +=1
        continue

    contagem_atual = frase.count(letra_atual)

    if contagem_atual == maior_aparecido:
        repetido = contagem_atual

    if contagem_atual > maior_aparecido:

        maior_aparecido = contagem_atual
        indice_do_mais_aparecido = i
    i += 1

print(f"A letra que mais apareceu é [{frase[indice_do_mais_aparecido]}] com {maior_aparecido} aparições")

if repetido == maior_aparecido:
    print(f"Porém a letra {frase[repetido]} aparece a mesma quantidade vezes")