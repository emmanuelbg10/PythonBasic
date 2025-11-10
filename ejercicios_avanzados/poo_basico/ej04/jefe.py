from empleado import Empleado
from typing import List

class Jefe(Empleado):
    def __init__(self, nombre, edad, salario, departamento, empleados_a_cargo: List[Empleado]):
        super().__init__(nombre, edad, salario, departamento)
        self.empleados_a_cargo = empleados_a_cargo

    def info_persona(self):
        return f"{super().info_persona()}, numero de empleados a cargo: {len(self.empleados_a_cargo)}"