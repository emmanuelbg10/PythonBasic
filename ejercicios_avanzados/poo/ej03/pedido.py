class Pedido:
    def __init__(self, productos):
        self.__productos = productos.copy()
        self.__total = self._calcular_total()

    def _calcular_total(self):
        return sum(p["precio"] * p["cantidad"] for p in self.__productos)

    @property
    def productos(self):
        return self.__productos

    @property
    def total(self):
        self.__total = self._calcular_total()
        return self.__total

    @productos.setter
    def productos(self, nuevos_productos):
        self.__productos = nuevos_productos.copy()
        self.__total = self._calcular_total()

    def agregar(self, nombre_producto, precio, cantidad):
        if precio < 0 or cantidad < 0:
            print("Precio o cantidad menor a 0, agregacion no valida\n")
            return 
        
        nuevo = {"nombre": nombre_producto, "precio": float(precio), "cantidad": int(cantidad)}
        self.__productos.append(nuevo)             
        self.__total += nuevo["precio"] * nuevo["cantidad"]

    def eliminar(self, indice):
        eliminado = self.__productos.pop(indice)  
        self.__total -= eliminado["precio"] * eliminado["cantidad"]

    def __str__(self):
        if not self.__productos:
            productos_str = "(sin productos)"
        else:
            productos_str = "\n".join(
                f"nombre: {p['nombre']}, precio: {p['precio']:.2f}€, cantidad: {p['cantidad']}, subtotal: {p['precio'] * p['cantidad']:.2f}€"
                for p in self.__productos
            )
        return f"Productos:\n{productos_str}\nTotal: {self.total:.2f}€"


if __name__ == "__main__":
    pedidos = [
        {"nombre" : "manzanas", "precio" : 2.99, "cantidad" : 2},
        {"nombre" : "platanos", "precio" : 3.50, "cantidad" : 8},
        {"nombre" : "peras", "precio" : 4.20, "cantidad" : 6},
        {"nombre" : "aguacates", "precio" : 7.99, "cantidad" : 3}
    ]

    huerta = Pedido(pedidos)

    print("\nListando huerta, sus productos y el total")
    print(huerta)

    print("\nAgregando un producto a la huerta con su precio y analizando los cambios")
    huerta.agregar("patatas", 2.33, -1)
    print(huerta)

    print("\nEliminando un producto en la huerta con su precio y analizando los cambios")
    huerta.eliminar(1)
    print(huerta)
