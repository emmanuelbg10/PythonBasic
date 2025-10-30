class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
        self.edad = 0 

    def mostrar_nombre(self):
        print(f"Mi nombre es {self.nombre}")
        

persona = Persona("Emmanuel")
persona.mostrar_nombre()

print("Edad actual (sin modificar):", persona.edad)

persona.edad = 20
print("Edad actual (modificada):", persona.edad)


