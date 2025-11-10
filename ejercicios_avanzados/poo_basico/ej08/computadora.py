from dispositivo import Dispositivo

class Computadora(Dispositivo):
    def __init__(self, estado = "encendido"):
        super().__init__(estado)

    def encender(self):
        self.estado = "encendido"
        print(f"Se ha {self.estado} la computadora")
    
    def apagar(self):
        self.estado = "apagado"
        print(f"Se ha {self.estado} la computadora")