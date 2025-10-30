from abc import ABC, abstractmethod

class OperacionFinanciera(ABC):
    def __init__(self, monto, fecha):
        self.monto = monto
        self.fecha = fecha

    @abstractmethod
    def validar(self):
        pass

    @abstractmethod
    def ejecutar(self):
        pass


    