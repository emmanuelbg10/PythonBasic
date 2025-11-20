import os
import csv
from typing import List


class Empleado:
    def __init__(self, nombre, edad, departamento):
        self.nombre = nombre
        self.edad = edad
        self.departamento = departamento

    @classmethod
    def leer_empleados(cls):
        empleados = []

        ruta = os.path.dirname(__file__)
        archivo = os.path.join(ruta, "empleados.csv")

        with open(archivo, encoding="utf-8") as file:
            csv_reader = csv.reader(file, delimiter=";")
            next(csv_reader)

            for fila in csv_reader:
                nombre, edad, departamento = fila
                empleados.append(cls(nombre, edad, departamento))

        return empleados


def guardar_empleados(empleados: List[Empleado]):
    ruta = os.path.dirname(__file__)
    archivo = os.path.join(ruta, "empleados.csv")
    with open(archivo, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(["nombre", "edad", "departamento"])

        for empleado in empleados:
            writer.writerow([empleado.nombre, empleado.edad, empleado.departamento])


def filtrar_empleados(departamento):
    empleados_filtrados = []

    empleados: List[Empleado] = Empleado.leer_empleados().copy()

    for empleado in empleados:
        if departamento.lower() == empleado.departamento.lower():
            empleados_filtrados.append(empleado)

    return empleados_filtrados


def mostrar_empleados(empleados: List[Empleado]):
    for empleado in empleados:
        print(f"{empleado.nombre}, {empleado.edad}, {empleado.departamento}")


e1 = Empleado("Ana López", 28, "Recursos Humanos")
e2 = Empleado("Emmanuel Barral", 20, "IT")
e3 = Empleado("Lucía García", 42, "Marketing")

lista_empleados = [e1, e2, e3]

guardar_empleados(lista_empleados)
empleados = Empleado.leer_empleados()

print("Empleados:")
mostrar_empleados(empleados)

print("\nEmpleados filtrados por departamento IT:")
mostrar_empleados(filtrar_empleados("it"))

print("\nEmpleados filtrados por departamento inventado:")
# no pasara nada porque intentara mostrar una lista vacia
mostrar_empleados(filtrar_empleados("ia"))
