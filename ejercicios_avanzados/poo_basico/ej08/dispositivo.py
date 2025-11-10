from abc import ABC, abstractmethod

class Dispositivo(ABC):
    def __init__(self, estado):
        self.estado = estado
        
    @abstractmethod
    def encender(self):
        pass

    @abstractmethod
    def apagar(self):
        pass