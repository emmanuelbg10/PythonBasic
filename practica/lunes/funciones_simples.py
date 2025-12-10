import random

# ------------------------------------------------------------------------------------
print("PASO1: funcion q sume los numeros de una lista")
lista = list(random.randint(1, 100) for _ in range(20))
print(lista)


def suma(lista):
    result = 0
    for num in lista:
        result += num

    return result


print(suma(lista))

# ------------------------------------------------------------------------------------
print("\nPASO2: funcion q muestre los pares de una lista")
print(list(filter(lambda num: num % 2 == 0, lista)))
# ------------------------------------------------------------------------------------
print("\nPASO3: funcion: recibe una lista de strings y devuelve la palabra mas larga")
palabras = ["hola", "buenas", "que", "tal"]


def texto_largo(palabras):
    result = palabras[0]
    for palabra in palabras:
        if len(result) < len(palabra):
            result = palabra
    return result


print(texto_largo(palabras))
# ------------------------------------------------------------------------------------
