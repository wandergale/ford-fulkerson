from collections import defaultdict
from queue import Queue

class Grafo:
    def __init__(self):
        self.grafo = defaultdict(list)
    
    def adicionar_aresta(self, u, v):
        self.grafo[u].append(v)
        self.grafo[v].append(u)
    
    def verificar_bipartido(self):
        if not self.grafo:
            return False
        
        visitados = {}
        grupos = {}
        fila = Queue()
        
        # Inicializa o primeiro vértice com a cor 0
        primeiro_vertice = next(iter(self.grafo))
        grupos[primeiro_vertice] = 0
        fila.put(primeiro_vertice)
        
        while not fila.empty():
            vertice_atual = fila.get()
            
            for vizinho in self.grafo[vertice_atual]:
                if vizinho not in visitados:
                    visitados[vizinho] = True
                    
                    # Atribui uma cor oposta aos vértices adjacentes
                    grupos[vizinho] = 1 - grupos[vertice_atual]
                    
                    fila.put(vizinho)
                elif grupos[vizinho] == grupos[vertice_atual]:
                    # Encontrou um conflito de cores, o grafo não é bipartido
                    return False
        
        return True, grupos

# Função para criar o grafo com base nos pares ordenados
def criar_grafo(pares_ordenados):
    grafo = Grafo()
    
    for par in pares_ordenados:
        u, v = par
        grafo.adicionar_aresta(u, v)
    
    return grafo

# Exemplo de uso
pares = [(0,1),(0,2),(0,5),(1,3),(3,5),(4,5),(4,6),(0,6),(6,7),(7,8),(8,10),(9,10),(9,11),(10,12),(11,12)]
meu_grafo = criar_grafo(pares)
eh_bipartido, grupos = meu_grafo.verificar_bipartido()

if eh_bipartido:
    grupo_1 = [vertice for vertice, grupo in grupos.items() if grupo == 0]
    grupo_2 = [vertice for vertice, grupo in grupos.items() if grupo == 1]
    
    print("O grafo é bipartido.")
    print("Grupo 1:", grupo_1)
    print("Grupo 2:", grupo_2)
else:
    print("O grafo não é bipartido.")
