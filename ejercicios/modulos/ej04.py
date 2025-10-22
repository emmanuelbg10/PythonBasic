import random

conteo = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

for i in range(10):
    lanzamiento = random.randint(1, 6)
    print(f"Lanzamiento {i+1}: {lanzamiento}")
    conteo[lanzamiento] += 1

print("\nResultado:")
for numero, cantidad in conteo.items():
    print(f"{numero} : {cantidad} veces\n")
