from vehiculos import VehiculoAutonomo

class Dron(VehiculoAutonomo):
    def __init__(self, nombre, tipo_motor, capacidad_bateria):
        super().__init__()
        self.nombre = nombre
        self.tipo_motor = tipo_motor
        self.capacidad_bateria = capacidad_bateria 

    def iniciar_sistema_navegacion(self):
        return f"Sistema de navegación del dron {self.nombre} iniciado"

    def mover(self):
        return f"El dron {self.nombre} está moviéndose"
    
    def detener(self):
        return f"El dron {self.nombre} está detenido"

    def calcular_autonomia(self):
        if self.tipo_motor == 'electrico':
            return self.capacidad_bateria * 2
        elif self.tipo_motor == 'hibrido':
            return self.capacidad_bateria * 3
        else:
            return self.capacidad_bateria * 1.5
