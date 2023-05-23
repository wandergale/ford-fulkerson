class Grafo:
    n_arestas = 0
    m_vertices = 0
    matriz = 0

    def __init__(self, n_arestas, m_vertices):
        self.n_arestas = n_arestas
        self.m_vertices = m_vertices
        self.matriz = [ [ 0 for i in range(n_arestas) ] for j in range(m_vertices) ]

    def __str__(self):
        graph = ''
        for i in range(self.m_vertices):
            for j in range(self.n_arestas):
                graph+=str(self.matriz[i][j])+ ' '
            graph+='\n'
        
        return graph

    def criar_aresta(self, vi, vj, e):
        self.matriz[vi][e] += 1
        self.matriz[vj][e] += 1
    
    def remover_aresta(self, vi, vj, e):
        self.matriz[vi][e] -= 1
        self.matriz[vj][e] -= 1
    
    def existe_aresta(self, vi, vj, e):
        return self.matriz[vi][e] != 0 and self.matriz[vj][e] != 0

    def get_aresta(self, vi, vj):
        for e in range(self.n_arestas):
            if self.existe_aresta(vi, vj, e):
                return e
        return -1

    def get_grau_vertice(self, vertice):
        grau = 0
        for a in range(self.n_arestas):
            grau += self.matriz[vertice][a]
        return grau
    
    def get_grau_grafo(self):
        grau = 0
        for v in range(self.m_vertices):
            grau += self.get_grau_vertice(v)
        return grau

    def tem_loop(self):
        for v in range(self.m_vertices):
            for a in range(self.n_arestas):
                if self.matriz[v][a] > 1:
                    return True
        return False

    def tem_aresta_paralelas(self):
        for a1 in range(self.n_arestas-1):
            arestas1 = []
            for v1 in range(self.m_vertices):
                arestas1.append(self.matriz[v1][a1])
            for a2 in range(a1+1, self.n_arestas):
                arestas2 = []
                for v2 in range(self.m_vertices):
                    arestas2.append(self.matriz[v2][a2])
                if arestas1 == arestas2:
                    return True
        return False

    def eh_simples(self):
        if self.tem_loop() or self.tem_aresta_paralelas():
            return False
        return True

g = Grafo(3, 4)
g.criar_aresta(0,1,0) #aresta 1
g.criar_aresta(0,2,0) #aresta 1
print(g)
print(g.existe_aresta(0,1,0))
print(g.get_aresta(0, 1))
print(g.get_grau_vertice(0))
print(g.get_grau_grafo())
print(g.tem_loop())
print(g.tem_aresta_paralelas())
print(g.eh_simples())