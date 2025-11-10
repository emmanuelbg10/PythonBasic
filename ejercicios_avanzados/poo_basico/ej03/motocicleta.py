from vehiculo import Vehiculo

class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, ano, tipo_manillar):
        super().__init__(marca, modelo, ano)
        self.tipo_manillar = tipo_manillar


    def info_vehiculo(self):
        return f"{super().info_vehiculo()}, Tipo de manillar: {self.tipo_manillar}"