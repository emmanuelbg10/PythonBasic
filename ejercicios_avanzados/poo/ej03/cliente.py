from pedido import Pedido

class Cliente:
    def __init__(self, nombre, pedido):
        if not isinstance(pedido, Pedido):
            raise TypeError("El pedido debe ser una instancia de la clase Pedido.")
        self.__nombre = nombre
        self.__pedido = pedido

    @property
    def nombre(self):
        return self.__nombre

    @property
    def total_pedido(self):
        return self.__pedido.total

    def ver_pedido(self):
        return str(self.__pedido)

    def __str__(self):
        return f"Cliente: {self.__nombre}\nTotal de su pedido: {self.total_pedido:.2f}€"


pedidos = [
    {"nombre": "manzanas", "precio": 2.99, "cantidad": 2},
    {"nombre": "plátanos", "precio": 3.50, "cantidad": 8},
]

productos_a_comprar = Pedido(pedidos)

cliente1 = Cliente("Laura", productos_a_comprar)

print(cliente1)  
print("\nDetalles del pedido del cliente:")
print(cliente1.ver_pedido())

