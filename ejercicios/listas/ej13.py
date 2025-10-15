from random import sample
from functools import reduce

# Crear una lista de 10 números aleatorios distintos entre 1 y 100, no se repiten con sample
lista = sample(range(1, 101), 10)

print(lista)

maximo = reduce(lambda a, b: a if a > b else b, lista)
minimo = reduce(lambda a, b: a if a < b else b, lista )

print(f"El valor maximo es: {maximo}, y el valor minimo es: {minimo}")