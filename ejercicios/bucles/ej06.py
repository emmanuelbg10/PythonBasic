num = int(input("Escribe un número: "))
result = 1

for i in range(1, num + 1):
    result *= i  # multiplicamos por cada número de 1 a num

print(f"El factorial es: {result}")
