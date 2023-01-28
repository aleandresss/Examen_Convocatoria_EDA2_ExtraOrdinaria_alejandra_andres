class Nodo:
    def __init__(self,nombre):
        self.nombre = nombre 
        self.arcos = []
    
    def append_arco (self,nodo_dest,costo):
        self.arcos.append(Arco(nodo_destino, costo))

class Grafo:
    def __init__ (self):
        self.nodos = []

    def append_nodo(self, nodo):
        self.nodos.append(nodo)

class Node:
  def _init_(self, nombre):
    self.nombre = nombre
    self.vecino = {}   
  def agregar_nodo(self, nodo, peso):
    self.vecino[nodo] = peso

#clase grafo
class Grafo:
    
    #constructor de la clase
    def _init_(self, vertices):
        self.V = vertices
        self.grafo = []
        self.padre = [i for i in range(vertices)]
        self.rango = [0 for i in range(vertices)]
        self.nombre_a_vertice = {}
        self.vertice_a_nombre = {}
    
    #agregar arista
    def agregar_arista(self, u, v, w):
        if u not in self.nombre_a_vertice:
            vertice = len(self.nombre_a_vertice)
            self.nombre_a_vertice[u] = vertice
            self.vertice_a_nombre[vertice] = u
        if v not in self.nombre_a_vertice:
            vertice = len(self.nombre_a_vertice)
            self.nombre_a_vertice[v] = vertice
            self.vertice_a_nombre[vertice] = v
        u = self.nombre_a_vertice[u]
        v = self.nombre_a_vertice[v]
        self.grafo.append((u, v, w))
    
    
    def encontrar(self, i):
        if self.padre[i] == i:
            return i
        return self.encontrar(self.padre[i])
    
    
    def unir(self, x, y):
        xroot = self.encontrar(x)
        yroot = self.encontrar👍
        if self.rango[xroot] < self.rango[yroot]:
            self.padre[xroot] = yroot
        elif self.rango[xroot] > self.rango[yroot]:
            self.padre[yroot] = xroot
        else:
            self.padre[yroot] = xroot
            self.rango[xroot] += 1
    
    #Kruskal
    def kruskal(self):
        resultado = []
        i, e = 0, 0
        self.grafo = sorted(self.grafo, key=lambda x: x[2])
        while e < self.V - 1:
            u, v, w = self.grafo[i]
            i = i + 1
            x = self.encontrar(u)
            y =self.encontrar(v)
            if x != y:
                e = e + 1
                resultado.append((u, v, w))
                self.unir(x, y)
        return resultado