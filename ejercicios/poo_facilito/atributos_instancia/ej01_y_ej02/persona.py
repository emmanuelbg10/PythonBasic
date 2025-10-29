class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
        self.__edad = 0 

    def mostrar_nombre(self):
        print(f"Mi nombre es {self.nombre}")
        
    def modificar_edad(self, nueva_edad):
        self.edad = nueva_edad

persona = Persona("Emmanuel")
persona.mostrar_nombre()

print("Edad actual (sin modificar):", persona.edad)

persona.modificar_edad(20)
print("Edad actual (modificada):", persona.eda)


