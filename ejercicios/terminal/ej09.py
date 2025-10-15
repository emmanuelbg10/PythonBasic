print("Vamos a calcular todas las operaciones basicas con 2 numeros que escribas")
num1 = float(input("Escribe un numero: "))
num2 = float(input("Escribe otro numero: "))

operaciones = {
    "suma": lambda x, y: x + y,
    "resta": lambda x, y: x - y,
    "multiplicacion": lambda x, y: x * y,
    "division": lambda x, y: x / y if y != 0 else 0
}

for nombre, operacion in operaciones.items():
    print(f"La {nombre} de estos 2 numeros es: {operacion(num1, num2)}")
