edades = [13, 20, 80, 45, 15, 18]

print(f"Lista de edades: {edades}")

mayores = list(filter(lambda edad: edad >= 18, edades))

print(f"Lista de edades mayores de edad: {mayores}")