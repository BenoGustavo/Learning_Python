# Sistema de perguntas e respostas

acertos = 0
contador = 0

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '3',
    },
    {
        'Pergunta': 'Quanto é 9*9?',
        'Opções': ['83', '82', '90', '81'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Qual o dia do natal?',
        'Opções': ['1/1', '25/12', '25/11', '1/12'],
        'Resposta': '2',
    },
    {
        'Pergunta': 'Qual o alimento com mais denso em proteinas?',
        'Opções': ['Peito de frango', 'Peito de peru', 'Carne bovina', 'Salmão'],
        'Resposta': '1',
    }
]

print("-=-"*5, 'Perguntas e respostas', "-=-"*5, '\n')

for i in range(0, len(perguntas)):

    print(perguntas[i]['Pergunta'])

    print("Opções:")

    contador = 1
    for chaves in perguntas[i]['Opções']:
        print(contador, ") ", chaves, sep='')
        contador += 1
    resp = input("Escolha uma opção: ")

    if resp is perguntas[i]['Resposta']:
        print("\nParabens, Você acertou !!!\n")
        acertos += 1
    else:
        print("\nResposta incorreta, mais sorte na proxima...\n")

if acertos == 4:
    print("Parabéns, você acertou todas as perguntas...")
elif acertos > 0:
    print(f"Você acertou {acertos}/4")
else:
    print("Você não acertou nenhuma pergunta, mais sorte na proxima")
