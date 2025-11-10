from animal import Animal

class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, "Perro", edad)
        self.raza = raza

    def hacer_sonido(self):
        return "Guau, guau!!"

