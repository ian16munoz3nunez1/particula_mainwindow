from Particula.particula import Particula

class MainClass:
    def __init__(self):
        self.__particulas = []
    def agregar_inicio(self, particula: Particula):
        self.__particulas.insert(0, particula)
    def agregar_final(self, particula: Particula):
        self.__particulas.append(particula)
    def imprimir(self):
        for particula in self.__particulas:
            print(particula)
    def __str__(self):
        return "".join(
            str(particula) for particula in self.__particulas
        )
