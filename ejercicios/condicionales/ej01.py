num = int(input("Escribe un numero: "))
result = "positivo" if num > 0 else ("negativo" if num < 0 else "cero") #operador ternario
print(f"Tu numero es {result}")