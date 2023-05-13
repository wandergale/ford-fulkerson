from math import inf

class Grafo:
  n = 0
  adjacencia = None

  def __init__(self,n):
    self.n = n
    self.adjacencia = [None]*n
    for i in range(n):
      self.adjacencia[i] = [0]*n

  def __str__(self):
    graph = ''
    for i in range(self.n):
      graph+=' v'+str(i)+ '-> '
      for j in range(len(self.adjacencia[i])):
        graph+= str(self.adjacencia[i][j])+'  '
      graph+='\n'
    return graph

  def criar_aresta(self, vi, vj, v):
    self.adjacencia[vi][vj] = v
  
  def visitas(self, source, sink, parent):
    visitado = [False] * self.n
    pilha = [[source, float(inf)]]
  
    while pilha:
        # print('antes ', pilha)
        u, fluxo = pilha.pop()
        # print('depois ', pilha, u, fluxo)
        # print(visitado)
        visitado[u] = True
        for aresta, var in enumerate(self.adjacencia[u]):
            # print(aresta, var)
            if visitado[aresta] == False and var > 0:
                if aresta == sink:
                    parent[aresta] = u
                    return fluxo
                pilha.append([aresta, min(fluxo, var)])
                parent[aresta] = u
    return 0
  
  def ford_fulkerson(self, source, sink):
    parent = [-1] * self.n
    max_fluxo = 0
    
    while True:
        path_fluxo = self.visitas(source, sink, parent)
        # print(path_fluxo)
        if path_fluxo == 0:
            break
        max_fluxo += path_fluxo
    
        v = sink
        while v != source:
            u = parent[v]
            self.adjacencia[u][v] -= path_fluxo
            self.adjacencia[v][u] += path_fluxo
        
            v = parent[v]
    
    return max_fluxo
  
g = Grafo(6)
g.criar_aresta(0,1, 16)
g.criar_aresta(0, 2, 13)
g.criar_aresta(1, 2, 10)
g.criar_aresta(1, 3, 12)
g.criar_aresta(2, 1, 4)
g.criar_aresta(2, 4, 14)
g.criar_aresta(3, 2, 9)
g.criar_aresta(3, 5, 20)
g.criar_aresta(4, 3, 7)
g.criar_aresta(4, 5, 4)
source = 0
sink = 5
print(g)
print()
print(g.adjacencia)
fluxo_maximo = g.ford_fulkerson(source, sink)
print('Fluxo máximo: ', fluxo_maximo)