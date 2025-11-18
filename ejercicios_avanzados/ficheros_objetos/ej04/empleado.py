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
        ruta = os.path.dirname(__file__)
        archivo = os.path.join(ruta, "empleados.csv")
        with open(archivo) as file:
            csv_reader = csv.reader(file, delimiter=";")
            next(csv_reader)
            for fila in csv_reader:
                nombre, edad, departamento = fila
                print(nombre, edad, departamento)



def guardar_empleados(empleados: List[Empleado]):
    ruta = os.path.dirname(__file__)
    archivo = os.path.join(ruta, "empleados.csv")
    with open(archivo, "w", newline="" ,encoding="utf-8") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(["nombre", "edad", "departamento"])

        for empleado in empleados:
            writer.writerow([empleado.nombre, empleado.edad, empleado.departamento])

e1 = Empleado("Ana López", 28, "Recursos Humanos")
e2 = Empleado("Emmanuel Barral", 20, "IT")
e3 = Empleado("Lucía García", 42, "Marketing")

lista_empleados = [e1, e2, e3]

guardar_empleados(lista_empleados)
Empleado.leer_empleados()


    