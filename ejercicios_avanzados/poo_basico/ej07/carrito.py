from metodo_pago import MetodoPago

class Carrito:
    def __init__(self):
        self.items = []
        self.total = 0

    def agregar_item(self, nombre, precio):
        self.items.append({"nombre": nombre, "precio": precio})
        self.total += precio

    def mostrar_items(self):
        for item in self.items:
            print(f"{item['nombre']}: {item['precio']:.2f}€")
        print(f"Total: {self.total:.2f}€")

    def procesar_pago(self, metodo_pago: MetodoPago):
        print(metodo_pago.procesar_pago(self.total))
