class Vehiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def info_vehiculo(self):
        return f"Su marca es: {self.marca}, su modelo es: {self.modelo}, su año es: {self.ano}"