def ache_no_custo_mais_baixo(custos, processados):
    custo_mais_baixo = float("inf")
    no_com_custo_mais_baixo = None
    for no in custos:
        custo = custos[no]
        if custo < custo_mais_baixo and no not in processados:
            custo_mais_baixo = custo
            no_com_custo_mais_baixo = no
    return no_com_custo_mais_baixo

def grafo_de_custo():
    grafo :dict = {}
    grafo["inicio"] = {}
    grafo["inicio"]["a"] = 6
    grafo["inicio"]["b"] = 2
    
    grafo["a"] = {}
    grafo["a"]["fim"] = 1

    grafo["b"] = {}
    grafo["b"]["a"] = 3
    grafo["b"]["fim"] = 5

    grafo["fim"] = {}

    return grafo

def dijkstra(grafo):
    custos = {}
    for no in grafo:
        custos[no] = float("inf")
    custos["inicio"] = 0

    processados = []

    no = ache_no_custo_mais_baixo(custos, processados)
    while no is not None:
        custo = custos[no]
        vizinhos = grafo[no]
        for no_vizinho in vizinhos.keys():
            novo_custo = custo + vizinhos[no_vizinho]
            if custos[no_vizinho] > novo_custo:
                custos[no_vizinho] = novo_custo
        processados.append(no)
        no = ache_no_custo_mais_baixo(custos, processados)
    return custos

def grafo_exercicio():
    grafo :dict = {}
    grafo["inicio"] = {}
    grafo["inicio"]["a"] = 5
    grafo["inicio"]["b"] = 2

    grafo["a"] = {}
    grafo["a"]["b"]

if __name__ == "__main__":
    print("Grafo de inicio")
    print(grafo_de_custo()["inicio"])
    print("Grafo de a")
    print(grafo_de_custo()["a"])
    print("Grafo de b")
    print(grafo_de_custo()["b"])

    print(dijkstra(grafo_de_custo()))