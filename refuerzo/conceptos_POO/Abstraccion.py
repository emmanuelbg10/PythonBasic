from abc import ABC, abstractmethod

class Vehiculo(ABC):
    @abstractmethod
    def conducir(self):
        pass

class Coche(Vehiculo):
    def conducir(self):
        return "Conduciendo un coche"

class Moto(Vehiculo):
    def conducir(self):
        return "Conduciendo una moto"

# Uso
vehiculos = [Coche(), Moto()]
for v in vehiculos:
    print(v.conducir())   