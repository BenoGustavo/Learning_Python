from itertools import groupby

#Maneira de ordenar a lista + EX de lambda em dicionarios

ORDEM = lambda a: a['nota']

#Forma pratica de mostrar os dados

def print_iter_notas(list): 
    for key, group in  list:
        print(key)
        for pupil in group:
            print(pupil)

#Lista de dados

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
]

#Função sorted para deixar a lista em ordem maior nota

alunos_ordenado_por_nota = sorted(alunos, key=ORDEM)

#Criar grupos de alunos pela nota

grupos = groupby(alunos_ordenado_por_nota, key=ORDEM)

print_iter_notas(grupos)