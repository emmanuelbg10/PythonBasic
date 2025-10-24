nombres = ["Emmanuel", "Pepe", "Pepon", "Julian", "Ana", "Pedro"]
edades = [20, 35, 93, 12, 40, 10]

diccionario = {x : y for x, y in zip(nombres, edades)}

print(diccionario)