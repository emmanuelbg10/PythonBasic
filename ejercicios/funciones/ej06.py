def area_rectangulo(base, altura):
    return base * altura

base = float(input("Escribe la base del rectángulo: "))
altura = float(input("Escribe la altura del rectángulo: "))

print(f"El área del rectángulo es: {area_rectangulo(base, altura)}")

print("Pruebas adicionales:")
print(f"Área con base=5 y altura=3: {area_rectangulo(5, 3)}")
print(f"Área con base=10 y altura=2: {area_rectangulo(10, 2)}")
print(f"Área con base=7.5 y altura=4.2: {area_rectangulo(7.5, 4.2)}")
