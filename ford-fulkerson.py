from math import inf

class Grafo:
  n = 0
  adjacencia = None

  def __init__(self,n):
    self.n = n
    self.adjacencia = [None]*n
    for i in range(n):
      self.adjacencia[i] = []

  def __str__(self):
    graph = ''
    for i in range(self.n):
      graph+=' v'+str(i)+ '-> '
      for j in range(len(self.adjacencia[i])):
        graph+= str(self.adjacencia[i][j])+'  '
      graph+='\n'
    return graph

  def criar_aresta(self,vi,v):
    # print(self.adjacencia)
    self.adjacencia[vi].append(v)
  
  def visitas(self, source, sink, parent):
    visitado = [False] * self.n
    pilha = [[source, float(inf)]]
  
    while pilha:
        u, fluxo = pilha.pop()
        visitado[u] = True
        for ind, val in enumerate(self.adjacencia[u]):
            if visitado[ind] == False and val > 0:
                if ind == sink:
                    parent[ind] = u
                    return fluxo
                pilha.append([ind, min(fluxo, val)])
                parent[ind] = u
    return 0
  
  def ford_fulkerson(self, source, sink):
    parent = [-1] * self.n
    max_fluxo = 0
    
    path = True
    while path:
        path_fluxo = self.visitas(source, sink, parent)
        if path_fluxo == 0:
            path = False
        max_fluxo += path_fluxo
    
        v = sink
        while v != source:
            u = parent[v]
            self.adjacencia[u][v] -= path_fluxo
            self.adjacencia[v][u] += path_fluxo
        
            v = parent[v]
    
    return max_fluxo
  
g = Grafo(6)
g.criar_aresta(0, 0)
g.criar_aresta(0,16)
g.criar_aresta(0, 13)
g.criar_aresta(0, 0)
g.criar_aresta(0, 0)
g.criar_aresta(0, 0)
g.criar_aresta(1, 0)
g.criar_aresta(1, 0)
g.criar_aresta(1, 10)
g.criar_aresta(1,12)
g.criar_aresta(1, 0)
g.criar_aresta(1, 0)
g.criar_aresta(2, 0)
g.criar_aresta(2, 4)
g.criar_aresta(2, 0)
g.criar_aresta(2, 0)
g.criar_aresta(2, 14)
g.criar_aresta(2, 0)
g.criar_aresta(3, 0)
g.criar_aresta(3, 0)
g.criar_aresta(3, 9)
g.criar_aresta(3, 0)
g.criar_aresta(3, 0)
g.criar_aresta(3, 20)
g.criar_aresta(4, 0)
g.criar_aresta(4, 0)
g.criar_aresta(4, 0)
g.criar_aresta(4, 7)
g.criar_aresta(4, 0)
g.criar_aresta(4, 4)
g.criar_aresta(5, 0)
g.criar_aresta(5, 0)
g.criar_aresta(5, 0)
g.criar_aresta(5, 0)
g.criar_aresta(5, 0)
source = 0
sink = 5

max_fluxo = g.ford_fulkerson(source, sink)
print(max_fluxo)