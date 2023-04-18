import json

pessoa = {
    'nome': 'Gustavo',
    'sobrenome': 'Gorges',
    'enderecos': [
        {'rua': 'R1', 'numero': 32},
        {'rua': 'R2', 'numero': 55},
    ],
    'altura': 1.8,
    'numeros_preferidos': (2, 4, 6, 8, 10),
    'dev': True,
    'nada': None,
}

with open('arquivos_em_json.json','w',encoding='utf8') as arquivo:
    json.dump(pessoa, arquivo, ensure_ascii=False, indent=2 ) #ensure_ascii (remover umas parada esquisitas) || indent=2 mantem indentação