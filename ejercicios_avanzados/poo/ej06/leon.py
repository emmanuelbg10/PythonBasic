from animal import Animal

class Leon(Animal):
    def __init__(self, nombre, edad):
        super().__init__(nombre, "León", edad)

    def emitir_sonido(self):
        return "¡Roaaarrr!"
    
    def alimentarse(self):
        return f"El león {self.nombre} está comiendo."
    
