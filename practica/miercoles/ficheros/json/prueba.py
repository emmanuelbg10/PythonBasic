import json
import os

ruta_actual = os.path.dirname(__file__)
archivo = os.path.join(ruta_actual, "prueba.json")


def leer_archivo(archivo):
    with open(archivo, "r", encoding="utf-8") as file:
        datos = json.load(file)
    return datos


fichero = leer_archivo(archivo)

profesores = []
estudiantes = []
for clave, valor in fichero.items():
    persona = valor[0]
    if "asignatura" in persona:
        profesores.append(persona)
    else:
        estudiantes.append(persona)

print(profesores)
print(estudiantes)


def guardar_archivo(lista, nombre_archivo):
    archivo = os.path.join(ruta_actual, nombre_archivo)

    with open(archivo, "w", encoding="utf-8") as file:
        json.dump(lista, file, indent=4, ensure_ascii=False)


guardar_archivo(profesores, "profesores.json")
