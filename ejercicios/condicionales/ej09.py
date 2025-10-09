print("Cine con descuento para diferentes edades:")
age = int(input("Escribe la edad de la persona: "))
price = float(input("Escribe el precio de la entrada: "))

final_price = price * 0.5 if age <= 12 else price * 0.7 if age >= 65 else price

print(f"El precio de la entrada es: {final_price}")