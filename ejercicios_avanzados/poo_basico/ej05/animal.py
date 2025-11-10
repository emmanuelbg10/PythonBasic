from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nombre, especie, edad):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
    
    @abstractmethod
    def hacer_sonido(self):
        pass
