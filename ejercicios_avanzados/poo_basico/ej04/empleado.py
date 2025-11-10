from persona import Persona

class Empleado(Persona):
    def __init__(self, nombre, edad, salario, departamento):
        super().__init__(nombre, edad)
        self.salario = salario
        self.departamento = departamento

    def info_persona(self):
        return f"{super().info_persona()}, su salario: {self.salario}€, su departamento: {self.departamento}"