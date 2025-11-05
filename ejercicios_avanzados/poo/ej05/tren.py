from vehiculo_transporte import VehiculoTransporte
class Tren(VehiculoTransporte):
    def __init__(self, capacidad, velocidad_max, metodos_aceptados, id):
        super().__init__(capacidad, velocidad_max, metodos_aceptados, id)

    def iniciar_viaje(self):
        return f"{super().iniciar_viaje()}, disfruten pasajeros del viaje en tren: {self.id}"
    
    def sistema_cobro(self, metodo_cobro, cantidad):
        return super().sistema_cobro(metodo_cobro, cantidad)