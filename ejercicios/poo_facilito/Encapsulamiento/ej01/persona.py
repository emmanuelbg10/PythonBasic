class Persona:
    def __init__(self, nombre):
        self.__nombre = nombre

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):  
        self.__nombre = nuevo_nombre

persona = Persona("Emmanuel")

print("Me llamo:",persona.nombre)  
persona.nombre = "Pepe"

print("Ahora me llamo:", persona.nombre)

