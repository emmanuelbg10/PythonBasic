numeros = [1, 2, 3, 4, 5, 1, 2, 7, 5, 6]

pares_unicos = {x for x in numeros if x % 2 == 0}

print(pares_unicos)