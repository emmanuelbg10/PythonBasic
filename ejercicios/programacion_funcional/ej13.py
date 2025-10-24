numeros = list(range(1,11))

cubos_mayores = list(map(lambda x: x ** 3, list(filter( lambda x: x > 5, numeros))))

print(cubos_mayores)