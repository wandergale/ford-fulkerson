# : (0,1),(0,2),(0,5),(1,3),(3,5),(4,5),(4,6),(0,6),(6,7),(7,8),(8,10),(9,10),(9,11),(10,12),(11,12)
from queue import Queue
class Grafo:
    n = 0
    matriz = 0

    def __init__(self, n):
        self.n = n
        self.matriz = [[0 for i in range(n)] for j in range(n)]

    def __str__(self):
        graph = ''
        for i in range(self.n):
            for j in range(self.n):
                graph += str(self.matriz[i][j]) + ' '
            graph +='\n'
        
        return graph

    def criar_aresta(self, vi, vj):
        self.matriz[vi][vj] += 1
        self.matriz[vj][vi] += 1

    def aresta_paralela(self):
        for i in range(self.n):
            for j in range(i+1, self.n):
                if self.matriz[i][j] > 1:
                    return self.matriz[i][j]
        return False
    
def verificar_bipartido(matriz, n):
    visitados = {}
    grupos = {}
    fila = Queue()

    # Inicializa o primeiro vértice com o grupo 0
    primeiro_vertice = 0
    grupos[primeiro_vertice] = 0
    fila.put(primeiro_vertice)

    while not fila.empty():
        vertice_atual = fila.get()

        for vizinho in range(n):
            if matriz[vertice_atual][vizinho] != 0:  # Verifica se há uma aresta entre os vértices
                if vizinho not in visitados:
                    visitados[vizinho] = True

                    # Atribui um grupo oposto aos vértices adjacentes
                    grupos[vizinho] = 1 - grupos[vertice_atual]

                    fila.put(vizinho)
                elif grupos[vizinho] == grupos[vertice_atual]:
                    # Encontrou um conflito de grupos, o grafo não é bipartido
                    return False

    return True, grupos

# def bipartido(grafo, n):
#     visitados = []
#     grupos = []
#     for i in range(n):
#         for vizinho in range(n):
#             if grafo.aresta_paralela():
#                 visitados[vizinho] = True
#                 grupos.append(grafo.aresta_paralela())
#             elif grupos[vizinho] == grupos[i]:
#                 return False
#     return True, grupos
n = 13
g = Grafo(n)
g.criar_aresta(0,1)
g.criar_aresta(0,2)
g.criar_aresta(0,5)
g.criar_aresta(1,3)
g.criar_aresta(3,5)
g.criar_aresta(4,5)
g.criar_aresta(4,6)
g.criar_aresta(0,6)
g.criar_aresta(6,7)
g.criar_aresta(7,8)
g.criar_aresta(8,10)
g.criar_aresta(9,10)
g.criar_aresta(9,11)
g.criar_aresta(10,12)
g.criar_aresta(11,12)
print(g)
eh_bipartido, grupos = verificar_bipartido(g.matriz, n)
print(eh_bipartido, grupos)