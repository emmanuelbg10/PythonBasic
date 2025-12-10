class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, nueva_edad):
        if nueva_edad > 0:
            self.__edad = nueva_edad

    def presentarse(self):
        return f"Hola, me llamo: {self.__nombre} y tengo {self.__edad}"


class Estudiante(Persona):
    def __init__(self, nombre, edad, notas=None):
        super().__init__(nombre, edad)
        self.notas = notas if notas is not None else []

    def promedio(self):
        if len(self.notas) == 0:
            return 0
        return sum(self.notas) / len(self.notas)


class Profesor(Persona):
    def __init__(self, nombre, edad, asignatura):
        self.asignatura = asignatura
        super().__init__(nombre, edad)

    def explicar(self):
        return f"Vamos a explicar la asignatura: {self.asignatura}"
