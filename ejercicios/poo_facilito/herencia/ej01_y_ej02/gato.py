from animal import Animal

class Gato(Animal):
    def __init__(self, nombre, raza):
        super().__init__(nombre)
        self.raza = raza

    def hablar(self):
        return f"El gato {self.nombre} de raza {self.raza} está maullando"

gato = Gato("Cati", "Siames")
print(gato.hablar())
