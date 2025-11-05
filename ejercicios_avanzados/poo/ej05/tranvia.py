from vehiculo_transporte import VehiculoTransporte
class Tranvia(VehiculoTransporte):
    def __init__(self, capacidad, velocidad_max, metodos_aceptados, id):
        super().__init__(capacidad, velocidad_max, metodos_aceptados, id)
        if velocidad_max > 80:
            raise ValueError("Un tranvia no puede tener una velocidad maxima de 80 km/h")

    def iniciar_viaje(self):
        return f"{super().iniciar_viaje()}, disfruten pasajeros del viaje en tranvia: {self.id}"
    
    def sistema_cobro(self, metodo_cobro, cantidad):
        return super().sistema_cobro(metodo_cobro, cantidad)