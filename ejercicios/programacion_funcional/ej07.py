precios = [0.99, 24.23, 3.99, 35, 50]

print(f"Precios normales: {precios}")

precios_con_iva = list(map(lambda x: round(x * 1.21, 2), precios))

print(f"\nPrecios con iva: {precios_con_iva}")