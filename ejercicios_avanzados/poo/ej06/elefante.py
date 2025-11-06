from animal import Animal

class Elefante(Animal):
    def __init__(self, nombre, edad):
        super().__init__(nombre, "Elefante", edad)

    def emitir_sonido(self):
        return "¡Brrruuuh!"
    
    def alimentarse(self):
        return f"El elefante {self.nombre} está comiendo."
    
