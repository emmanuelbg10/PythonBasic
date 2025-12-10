import random

# ----------------------------------------------------------------------------------
print("PASO1: nuevo diccionario solo de estudiantes con nota > 5")
estudiante1 = {"nombre": "Emmanuel", "nota": 10}
estudiante2 = {"nombre": "Joel", "nota": 4}
estudiante3 = {"nombre": "Juan", "nota": 8}
lista = [estudiante1, estudiante2, estudiante3]


def aprobados(diccionarios):
    return [diccionario for diccionario in diccionarios if diccionario["nota"] > 5]


print(aprobados(lista))
# ----------------------------------------------------------------------------------
print("\nPASO2: nueva lista cuadrados")

numeros = list(random.randint(1, 20) for _ in range(5))
print("Numeros:", numeros)


def al_cuadrado(numeros):
    return [num**2 for num in numeros]


print("Al cuadrado:", al_cuadrado(numeros))
