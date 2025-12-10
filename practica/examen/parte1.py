from abc import ABC, abstractmethod
import json
import os


class Persona(ABC):
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    @abstractmethod
    def presentarse(self):
        pass


class Estudiante(Persona):
    def __init__(self, nombre, edad, notas=None):
        super().__init__(nombre, edad)
        self.notas = notas if notas is not None else []

    def presentarse(self):
        return f"Hola me llamo {self.nombre} y tengo {self.edad}, soy estudiante"

    def promedio(self):
        if len(self.notas) == 0:
            return 0
        return sum(self.notas) / len(self.notas)


class Profesor(Persona):
    def __init__(self, nombre, edad, asignatura):
        super().__init__(nombre, edad)
        self.asignatura = asignatura

    def presentarse(self):
        return f"Hola me llamo {self.nombre} y tengo {self.edad}, soy profesor"

    def explicar(self):
        return f"Estoy enseñando {self.asignatura}"


estudiante1 = Estudiante("Emmanuel", 20, [9, 7, 10, 8.25])
estudiante2 = Estudiante("Paco", 34, [4, 6, 8, 2, 0])

profesor1 = Profesor("Luis", 57, "Mates")
profesor2 = Profesor("Pedro", 35, "Lengua")

estudiantes = [estudiante1, estudiante2]
profesores = [profesor1, profesor2]


def mostrar(lista):
    for dato in lista:
        print(dato.presentarse())
        if isinstance(dato, Profesor):
            print(dato.explicar())
        elif isinstance(dato, Estudiante):
            print(f"Nota promedio {dato.promedio():.2f}")


print("PARTE1:")
print("\nEstudiantes:")
mostrar(estudiantes)
print("\nProfesores:")
mostrar(profesores)

print("\nPARTE2:")

datos = {"estudiantes": estudiantes, "profesores": profesores}
print(datos)


promedio_total = sum([e.promedio() for e in datos["estudiantes"]]) / len(
    datos["estudiantes"]
)
profesores_mates = [x for x in datos["profesores"] if x.asignatura == "Mates"]
print(promedio_total)
for profesor in profesores_mates:
    print(profesor.explicar())

print("\nPARTE3:")

ruta_actual = os.path.dirname(__file__)
archivo = os.path.join(ruta_actual, "datos.json")

with open(archivo, "w", encoding="utf-8") as file:
    json.dump(
        [{"nombre": e.nombre, "edad": e.edad, "notas": e.notas} for e in estudiantes],
        file,
        indent=4,
        ensure_ascii=False,
    )
