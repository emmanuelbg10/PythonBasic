# Esto es un bucle del 0 al 9
# si la division la division del numero entre 2 su resto da 0 es par
# si no es impar y si es 5 es la mitad de 10

for i in range(10):
  if i == 5:
    print(f"{i} es la mitad de 10")
  elif i % 2 == 0:
    print(f"{i} es par")
  else:
    print(f"{i} es impar")