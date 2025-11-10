from animal import Animal

class Gato(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, "Gato", edad)
        self.raza = raza

    def hacer_sonido(self):
        return "Miau, miau!!"

