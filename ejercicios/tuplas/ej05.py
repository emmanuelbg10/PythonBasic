colores = ("rojo", "verde", "azul", "amarillo", "negro", "blanco")

color = input("Escribe un color: ") 

result = "" if color.lower() in colores else "no"

print(f"El color {color.lower()} {result} esta en la lista")