print("Escribe un numeros hasta escribir un numero negativo, cuando salgas se hará la suma")

result = 0

while True:
    num = float(input("Escribe un numero: "))

    if num < 0:
        break
    else:
        result += num
print(f"Resultado: {result}")

