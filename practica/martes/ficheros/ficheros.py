import os

ruta_actual = os.path.dirname(__file__)
archivo = os.path.join(ruta_actual, "datos.txt")
diccionario = {}
try:
    with open(archivo, "r") as file:
        for line in file:
            diccionario[line.strip()] = len(line.strip())

except OSError:
    print("No fue posible leer el archivo")

print(diccionario)


resultado = os.path.join(ruta_actual, "resultado.txt")

try:
    with open(resultado, "w") as file:
        for clave, valor in diccionario.items():
            file.write(f"{clave}: {valor}\n")
except OSError:
    print("No fue posible crear el archivo")
