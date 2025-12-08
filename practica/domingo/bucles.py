# ----------------------------------------------------------------------------
print("PASO1: Lista y clasificar entre par o impar")
lista = list(range(1, 21))

for num in lista:
    if num % 2 == 0:
        print(f"Par: {num}")
    else:
        print(f"Impar: {num}")
# ----------------------------------------------------------------------------
print("PASO2: detener al encontrar un multiplo de 7")
for n in lista:
    if n % 7 == 0:
        print(f"Multiplo de 7: {n}")
        break
    print(n)
# ----------------------------------------------------------------------------
print("PASO3: Saltarse los multiplos de 5")
for n in lista:
    if n % 5 == 0:
        continue
    print(n, end=", ")
