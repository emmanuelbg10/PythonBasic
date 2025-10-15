num1 = int(input("Escribe un numero: "))
num2 = int(input("Escribe otro numero: "))

suma = lambda x, y: x + y
print(f"La suma es: {suma(num1, num2)}")