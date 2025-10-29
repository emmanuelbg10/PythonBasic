from abc import ABC, abstractmethod

class VehiculoAutonomo(ABC):
    @abstractmethod
    def iniciar_sistema_navegacion(self):
        pass

    @abstractmethod
    def mover(self):
        pass

    @abstractmethod
    def detener(self):
        pass

    @abstractmethod
    def calcular_autonomia(self):
        pass