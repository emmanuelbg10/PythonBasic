price = float(input("Escribe el precio de un producto: "))

final_price = price * 0.9 if price > 100 else price

print(f"El precio final es: {final_price}")
