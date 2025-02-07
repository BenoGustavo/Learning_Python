estados_abranger = set([
    'mt','wa','or','id','nv','ut','ca','az'
])

estacoes = {}
estacoes['kum'] = set(['id','nv','ut'])
estacoes['kdois'] = set(['wa','id','mt'])
estacoes['ktres'] = set(['or','nv','ca'])
estacoes['kquatro'] = set(['nv','ut'])
estacoes['kcinco'] = set(['ca','az'])

def escolher_estacoes(estacoes, estados_abranger):
    estacoes_final = set()
    estados_cobertos = set()
    melhor_estacao = None;

    while estados_abranger:
        estados_cobertos = set()
        melhor_estacao = None
        for estacao, estados_por_estacao in estacoes.items():
            cobertos = estados_abranger & estados_por_estacao
            if len(cobertos) > len(estados_cobertos):
                melhor_estacao = estacao
                estados_cobertos = cobertos
        estacoes_final.add(melhor_estacao)
        estados_abranger -= estados_cobertos
    return estacoes_final

if __name__ == "__main__":
    print(escolher_estacoes(estacoes, estados_abranger))

