class Perro:
    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza

perro = Perro("Lukas", "Labrador")

print(f"El perro {perro.nombre} tiene esta raza: {perro.raza}")
