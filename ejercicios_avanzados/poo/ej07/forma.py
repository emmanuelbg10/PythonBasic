from abc import ABC, abstractmethod

class Forma(ABC):
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def dibujar(self):
        pass

