import os

ruta_actual = os.path.dirname(__file__)
archivo = os.path.join(ruta_actual, "prueba.txt")

estudiantes = []
profesores = []

try:
    with open(archivo, "r") as file:
        for line in file:
            line = line.strip()

            if "-" not in line:
                continue

            nombre, clave = [x.strip() for x in line.split("-")]

            if "Profesor" in clave:
                profesores.append(nombre)
            elif "Estudiante" in clave:
                estudiantes.append(nombre)

except OSError:
    print("No fue posible leer el archivo")

print(profesores)
print(estudiantes)


def crear(lista, nombre_archivo):
    archivo = os.path.join(ruta_actual, nombre_archivo)

    try:
        with open(archivo, "w") as file:
            for nombre in lista:
                file.write(f"{nombre}\n")

    except OSError:
        print("No fue posible crear el archivo")


crear(profesores, "profesores.txt")
crear(estudiantes, "estudiantes.txt")
