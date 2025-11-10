class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def info_persona(self):
        return f"Su nombre: {self.nombre}, su edad: {self.edad} años"

