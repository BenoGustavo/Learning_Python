from random import randint
import os

letras_validas = 'abcdefghijklmnopqrstuvwxyzç'
lista_palavras_secreta = ['paralelepipedo','maça','banana','refresco','tchola']
palavra_secreta = lista_palavras_secreta[randint(0,len(lista_palavras_secreta)-1)]
erros = 0
lista_erros = []
lista_acertos = []
tentativa = ''
acertos_em_ordem = ''

while True:

    #vitoria por quantidade de acertos

    if acertos_em_ordem == palavra_secreta:
        os.system("cls")
        print(f"\n\nParabéns, você acertou a palavra com {erros} erros, a palavras era {palavra_secreta}")
        break

    # definindo jogada

    print(f"\n\nLetras erradas já utilizadas {lista_erros}. Quantidade de erros {erros}")
    print(f"Letras acertadas {acertos_em_ordem}")
    print("Para sair digite 'Sair' || Para saber quantidade de letras digite 'Dica' \n")

    tentativa = input("Insira seu chute de letra ou chute uma palavra(Sem acentos): ")
    tentativa = tentativa.lower()

    if tentativa == 'dica':
        os.system("cls")
        print(f"A palavra secreta tem {len(palavra_secreta)} letras")
        continue

    if tentativa == 'sair':
        break

    if tentativa == palavra_secreta:
        print(f"\n\nParabéns, você acertou a palavra com {erros} erros, a palavras era {palavra_secreta}")
        break

    # definindo erro de digitação

    if tentativa not in letras_validas:
        os.system("cls")
        print(f"\nA palavra secreta não é {tentativa}...")
        erros += 1
        continue

    # definindo repetição e erro

    if tentativa not in palavra_secreta and tentativa not in lista_erros:
        os.system("cls")
        print(f"A letra {tentativa} não foi encontrada na palavra")
        lista_erros.append(tentativa)
        erros += 1
        continue

    if tentativa in lista_erros:
        os.system("cls")
        print(f"O caracter {tentativa} já foi classificado como usado")
        erros += 1
        continue

    # definindo acerto

    if tentativa in palavra_secreta:
        os.system("cls")
        print(f"Você acertou, {tentativa} existe dentro da palavra secreta")
        lista_acertos.append(tentativa)

        acertos_em_ordem = ''

        for j in palavra_secreta:
            if j in lista_acertos:
                acertos_em_ordem += j
            else:
                acertos_em_ordem += '*'
        
        continue
