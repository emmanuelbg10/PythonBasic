numeros = list(range(1, 11))

print(f"Lista de numeros: {numeros}")

impares = list(filter(lambda x: x % 2 == 0, numeros))

print(f"Lista de numeros impares {impares}")