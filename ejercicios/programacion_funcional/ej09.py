productos = [
    {"nombre": "Pan", "precio": 1.2},
    {"nombre": "Leche", "precio": 0.99},
    {"nombre": "Huevos", "precio": 2.5},
    {"nombre": "Queso", "precio": 4.75}
]

precios = list(map(lambda x: x["precio"], productos))

print("Lista de productos:", productos)
print("\nLista de precios:", precios)
