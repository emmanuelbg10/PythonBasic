from vehiculos import VehiculoAutonomo

class Barco(VehiculoAutonomo):
    def __init__(self, nombre, tipo_motor, capacidad_combustible):
        super().__init__()
        self.nombre = nombre
        self.tipo_motor = tipo_motor  # electrico, hibrido, gasolina
        self.capacidad_combustible = capacidad_combustible  

    def iniciar_sistema_navegacion(self):
        return f"Sistema de navegación del barco {self.nombre} iniciado"

    def mover(self):
        return f"El barco {self.nombre} está moviéndose"
    
    def detener(self):
        return f"El barco {self.nombre} está detenido"

    def calcular_autonomia(self):
        if self.tipo_motor == 'electrico':

            return self.capacidad_combustible * 5
        elif self.tipo_motor == 'hibrido':

            return self.capacidad_combustible * 10
        else:  # gasolina
            return self.capacidad_combustible * 8