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
                graph += str(self.matriz[i][j])+' '
            graph+='\n'
        return graph
    
    def criar_aresta(self, vi, vj):
        self.matriz[vi][vj] += 1
        self.matriz[vj][vi] += 1

    def remover_aresta(self, vi, vj):
        self.matriz[vi][vj] += 1
        self.matriz[vj][vi] += 1

    def existe_aresta(self, vi, vj):
        return self.matriz[vi][vj] > 0
    
    def grau_vertice(self, vertice):
        grau = 0
        for v in range(self.n):
            grau += self.matriz[v][vertice]
        return grau

    def grau_grafo(self):
        grau = 0
        for v in range(self.n):
            grau += self.grau_vertice(v)
        return grau

    def tem_loop(self):
        for i in range(self.n):
            if self.matriz[i][i] != 0:
                return True
        return False

    def aresta_paralela(self):
        for i in range(self.n):
            for j in range(i+1, self.n):
                if self.matriz[i][j] > 1:
                    return True
        return False
    
    def eh_simples(self):
        if self.tem_loop() or self.aresta_paralela():
            return False
        return True
    

g = Grafo(4)
g.criar_aresta(0,1) #aresta 1
g.criar_aresta(0,1) #aresta 2
g.criar_aresta(1,2) #aresta 3
g.criar_aresta(2,3) #aresta 4
g.criar_aresta(0,3) #aresta 5
g.criar_aresta(3,3) #aresta 6
g.criar_aresta(1,3) #aresta 7
print(g)
print(g.existe_aresta(0, 1))
print(g.grau_vertice(1))
print(g.grau_grafo())
print(g.tem_loop())
print(g.aresta_paralela())
print(g.eh_simples())