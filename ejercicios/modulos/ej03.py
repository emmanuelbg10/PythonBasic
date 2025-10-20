import math

# Pedir al usuario un ángulo en radianes
angulo = float(input("Ingrese un ángulo en radianes: "))


seno = math.sin(angulo) 
coseno = math.cos(angulo)
tangente = math.tan(angulo)

# Mostrar resultados
print(f"Seno: {seno}")
print(f"Coseno: {coseno}")
print(f"Tangente: {tangente}")
