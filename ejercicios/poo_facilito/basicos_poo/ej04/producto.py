class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

producto = Producto("Manzana", 10)

print(f"El producto {producto.nombre} tiene este precio: {producto.precio}")
