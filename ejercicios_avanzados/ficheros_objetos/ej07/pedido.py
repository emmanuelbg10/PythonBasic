import os
from typing import List
import json


class Pedido:
    def __init__(self, id_pedido, cliente, productos: list[str]):
        self.id_pedido = id_pedido
        self.cliente = cliente
        self.productos = productos

    @classmethod
    def leer_apedidos(cls):
        pedidos = []

        ruta = os.path.dirname(__file__)
        archivo = os.path.join(ruta, "pedidos.json")

        with open(archivo, encoding="utf-8") as file:
            pedidos_leidos = json.load(file)

            for pedido in pedidos_leidos:
                pedidos.append(
                    cls(pedido["id_pedido"], pedido["cliente"], pedido["productos"])
                )
        return pedidos


def guardar_pedidos(pedidos_dict):
    ruta = os.path.dirname(__file__)
    archivo = os.path.join(ruta, "pedidos.json")

    with open(archivo, "w", encoding="utf-8") as file:
        json.dump(pedidos_dict, file, ensure_ascii=False, indent=4)


lista_pedidos = [
    Pedido(
        id_pedido=101, cliente="Ana Martínez", productos=["Manzanas", "Leche", "Pan"]
    ),
    Pedido(
        id_pedido=102, cliente="Juan Pérez", productos=["Huevos", "Arroz", "Tomates"]
    ),
    Pedido(
        id_pedido=103, cliente="Lucía Gómez", productos=["Café", "Azúcar", "Galletas"]
    ),
]

pedidos_dict = [
    {
        "id_pedido": pedido.id_pedido,
        "cliente": pedido.cliente,
        "productos": pedido.productos,
    }
    for pedido in lista_pedidos
]

guardar_pedidos(pedidos_dict)

pedidos: List[Pedido] = Pedido.leer_apedidos()
for i, pedido in enumerate(pedidos, start=1):
    print(f"Pedido{i}: {pedido.id_pedido}, {pedido.cliente}, {pedido.productos}")
