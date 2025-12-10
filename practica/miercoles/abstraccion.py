from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def hablar(self):
        pass

    @abstractmethod
    def mover(self):
        pass


class Perro(Animal):
    def __init__(self):
        super().__init__()

    def hablar(self):
        return "Guau"

    def mover(self):
        return "corro"


class Gato(Animal):
    def __init__(self):
        super().__init__()

    def hablar(self):
        return "Miau"

    def mover(self):
        return "camino"


lista = [Gato(), Perro()]

for animal in lista:
    print(animal.hablar())
    print(animal.mover())
