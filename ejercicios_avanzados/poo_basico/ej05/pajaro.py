from animal import Animal

class Pajaro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, "Pajaro", edad)
        self.raza = raza

    def hacer_sonido(self):
        return "Piii, piii!!"

