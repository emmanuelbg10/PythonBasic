from vehiculo import Vehiculo

class Auto(Vehiculo):
    def __init__(self, marca, modelo, ano, numero_puertas = 4):
        super().__init__(marca, modelo, ano)
        self.numero_puertas = numero_puertas

    
    def info_vehiculo(self):
        return f"{super().info_vehiculo()}, Puertas: {self.numero_puertas}"