from animal import Animal

class Perro(Animal):
    def __init__(self, nombre, raza):
        super().__init__(nombre)
        self.raza = raza

    def hablar(self):
        return f"el perro {self.nombre} de raza {self.raza} está ladrando"

perro = Perro("lukas", "labrador")

print(perro.hablar())