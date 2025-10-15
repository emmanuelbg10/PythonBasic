num = int(input("Escribe un numero: "))

par = lambda x: True if x % 2 == 0 else False
resultado = "par" if par(num) else "impar"
print(f"Tu numero es {resultado}")