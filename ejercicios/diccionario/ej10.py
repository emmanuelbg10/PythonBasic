inventario = {
    "Producto1": {"nombre": "Manzanas", "precio": 1.5, "cantidad": 50},
    "Producto2": {"nombre": "Naranjas", "precio": 2.0, "cantidad": 30},
    "Producto3": {"nombre": "Peras", "precio": 1.8, "cantidad": 40},
    "Producto4": {"nombre": "Plátanos", "precio": 1.2, "cantidad": 60}
}

valor_total = 0
for producto in inventario.values():
    valor_total += producto["precio"] * producto["cantidad"]

print("El valor total del inventario es:", valor_total)
