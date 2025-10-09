num = int(input("Escribe un número del 0 al 100: "))

if 0 <= num <= 100:
    result = "A" if num >= 90 else "B" if num >= 80 else "C" if num >= 70 else "D" if num >= 60 else "F"
    print(f"Tu letra es: {result}")
else:
    print("Número inválido. Debe estar entre 0 y 100.")
