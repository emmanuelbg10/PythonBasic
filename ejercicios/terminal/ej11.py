price = float(input("Escribe el precio de un producto: "))
porcentaje_desc = float(input("Escribe el porcentaje del descuento: ")) / 100
valor_desc = price * porcentaje_desc
final_price = price - valor_desc

print(f"El precio final con el descuento es {final_price}")