import json
from criando_class import CAMINHO,pessoa

with open (CAMINHO,"r") as arquivo:
    all_info = json.load(arquivo)

    p1=pessoa(**all_info[0])
    p2=pessoa(**all_info[1])
    p3=pessoa(**all_info[2])

print(p1.nome,p1.sobrenome,p1.idade)
print(p2.nome,p2.sobrenome,p2.idade)
print(p3.nome,p3.sobrenome,p3.idade)