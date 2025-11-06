from animal import Animal

class Cebra(Animal):
    def __init__(self, nombre, edad):
        super().__init__(nombre, "Cebra", edad)

    def emitir_sonido(self):
        return "(sonido de cebra) xd"
    
    def alimentarse(self):
        return f"El elefante {self.nombre} está comiendo."
    
