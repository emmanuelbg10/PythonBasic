

print("Recomendar Ropa")
temp = float(input("Escribe la temperatura en celsius: "))

if temp < 10:
    result = "abrigo"
elif temp < 20:
    result = "chaqueta"
elif temp < 30:
    result = "manga corta"
else:
    result = "ropa ligera"

print(f"Te recomiendo usar {result}")