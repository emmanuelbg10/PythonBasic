class RedTransporte:
    def __init__(self):
        self.vehiculos = []

    def agregar_vehiculo(self, vehiculo):
        self.vehiculos.append(vehiculo)

    def iniciar_todos_viajes(self):
        for v in self.vehiculos:
            print(v.iniciar_viaje())

