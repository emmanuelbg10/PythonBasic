import os
import csv
from typing import List


class Producto:

    def __init__(self, id, nombre, precio):
        self.id = id
        self.nombre = nombre
        self.precio = float(precio)

    @classmethod
    def leer_productos(cls):
        productos = []
        ruta = os.path.dirname(__file__)
        archivo = os.path.join(ruta, "productos.csv")
        with open(archivo, encoding="utf-8") as file:
            csv_reader = csv.reader(file, delimiter=",")
            next(csv_reader)
            for fila in csv_reader:
                id, nombre, precio = fila
                productos.append(cls(id, nombre, precio))

        return productos


def guardar_productos(productos):
    ruta = os.path.dirname(__file__)
    archivo = os.path.join(ruta, "productos.csv")
    with open(archivo, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["id", "nombre", "precio"])

        for producto in productos:
            writer.writerow([producto.id, producto.nombre, producto.precio])


lista_productos = [
    Producto(1, "Teclado mecánico", 59.99),
    Producto(2, "Ratón inalámbrico", 24.50),
    Producto(3, "Monitor", 129.90),
]

guardar_productos(lista_productos)

productos: List[Producto] = Producto.leer_productos()
for producto in productos:
    print(f"{producto.id}, {producto.nombre}, {producto.precio}€")
