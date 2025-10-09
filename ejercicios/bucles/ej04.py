num = int(input("Escribe un numero: "))

print(f"Los numeros pares de {num} son: ")

for i in range(1, num + 1):
    if i % 2 == 0:
        print(i)
