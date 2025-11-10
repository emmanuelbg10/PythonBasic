from dispositivo import Dispositivo

class Smartphone(Dispositivo):
    def __init__(self, estado = "encendido"):
        super().__init__(estado)

    def encender(self):
        self.estado = "encendido"
        print(f"Se ha {self.estado} el smartphone")
    
    def apagar(self):
        self.estado = "apagado"
        print(f"Se ha {self.estado} el smartphone")