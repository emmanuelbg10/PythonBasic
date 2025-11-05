from vehiculo_transporte import VehiculoTransporte
class Autobus(VehiculoTransporte):
    def __init__(self, capacidad, velocidad_max, metodos_aceptados, id):
        super().__init__(capacidad, velocidad_max, metodos_aceptados, id)
        if velocidad_max > 100:
            raise ValueError("Un autobus no puede tener una velocidad maxima de 100 km/h")

    def iniciar_viaje(self):
        return f"{super().iniciar_viaje()}, disfruten pasajeros del viaje en autobus: {self.id}"
    
    def sistema_cobro(self, metodo_cobro, cantidad):
        return super().sistema_cobro(metodo_cobro, cantidad)
    
