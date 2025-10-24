nombres = ["manzana", "pera", "platano", "aguacate"]
precios = [2.99, 0.99, 2.5, 6]

productos = list(map(lambda n, p: (n, p), nombres, precios))

print("Lista de tuplas:", productos)
