from leon import Leon
from elefante import Elefante
from cebra import Cebra

class Zoologico:
    
    def __init__(self, animales):
        self.animales = animales
        self.especies_alimentadas = {}

    

    def actividad_diaria(self):
        for animal in self.animales:
            print()
            print(animal.emitir_sonido())
            print(animal.alimentarse())
            if animal.especie not in self.especies_alimentadas:
                self.especies_alimentadas[animal.especie] = 0
            self.especies_alimentadas[animal.especie] += 1

    def contador_alimento(self):
        print(self.especies_alimentadas)


simba = Leon("Simba", 5)
dumbo = Elefante("Dumbo", 2)
marty = Cebra("Marty", 7)
mufasa = Leon("Mufasa", 12)


lista_animales = [simba, dumbo, marty, mufasa]

zoo = Zoologico(lista_animales)

zoo.actividad_diaria()
zoo.contador_alimento()

