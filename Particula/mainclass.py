import json
from pprint import pformat
from collections import deque
from Particula.particula import Particula

class MainClass:
    def __init__(self):
        self.__particulas = []
    
    def agregar_inicio(self, particula: Particula):
        self.__particulas.insert(0, particula)
    
    def agregar_final(self, particula: Particula):
        self.__particulas.append(particula)
    
    def __str__(self):
        return "".join(
            str(particula) for particula in self.__particulas
        )

    def __len__(self):
        return len(self.__particulas)

    def __iter__(self):
        self.cont = 0
        return self

    def __next__(self):
        if self.cont < len(self.__particulas):
            particula = self.__particulas[self.cont]
            self.cont += 1
            return particula
        else:
            raise StopIteration

    def abrir(self, ubicacion):
        try:
            with open(ubicacion, 'r') as archivo:
                lista = json.load(archivo)
                self.__particulas = [Particula(**particula) for particula in lista]
            return 1
        except:
            return 0

    def guardar(self, ubicacion):
        try:
            with open(ubicacion, "w") as archivo:
                lista = [particula.to_dict() for particula in self.__particulas]
                json.dump(lista, archivo, indent=5)
            return 1
        except:
            return 0

    def crear_grafo(self, grafo):
        for particula in self.__particulas:
            origen_x = particula.origen_x
            origen_y = particula.origen_y
            destino_x = particula.destino_x
            destino_y = particula.destino_y
            distancia = particula.distancia

            origen = (origen_x, origen_y)
            destino = (destino_x, destino_y)
            arista_o = ((destino_x, destino_y), distancia)
            arista_d = ((origen_x, origen_y), distancia)

            if origen in grafo:
                grafo[origen].append(arista_o)
            else:
                grafo[origen] = [arista_o]
            if destino in grafo:
                grafo[destino].append(arista_d)
            else:
                grafo[destino] = [arista_d]
        str = pformat(grafo, width=50, indent=1)
        return str

    def busqueda_amplitud(self, grafo, origen_x=0, origen_y=0):
        self.crear_grafo(grafo)
        origen = (origen_x, origen_y)

        if origen in grafo:
            cola = deque()
            visitados = []
            recorrido = []

            cola.appendleft(origen)
            visitados.append(origen)

            while len(cola) > 0:
                vertice = cola[-1]
                recorrido.append(vertice)
                cola.pop()
                adyacente = grafo[vertice]
                for i in adyacente:
                    if not i[0] in visitados:
                        visitados.append(i[0])
                        cola.appendleft(i[0])
            return recorrido
        else:
            return 0

    def busqueda_profundidad(self, grafo, origen_x=0, origen_y=0):
        self.crear_grafo(grafo)
        origen = (origen_x, origen_y)

        if origen in grafo:
            pila = []
            visitados = []
            recorrido = []

            pila.append(origen)
            visitados.append(origen)

            while len(pila) > 0:
                vertice = pila[-1]
                recorrido.append(vertice)
                pila.pop()
                adyacente = grafo[vertice]
                for i in adyacente:
                    if not i[0] in visitados:
                        visitados.append(i[0])
                        pila.append(i[0])
            return recorrido
        else:
            return 0
