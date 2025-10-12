# Hallando el factorial de un numero
num = int(input("Escribe un número: "))
result = 1

for i in range(1, num + 1):
    result *= i 

print(f"El factorial es: {result}")
