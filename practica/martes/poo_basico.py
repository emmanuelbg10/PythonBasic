# ------------------------------------------------------------------------------------
print("PASO1: Estudiantes")


class Estudiante:
    def __init__(self, nombre, notas=None):
        self.__nombre = nombre
        self.__notas = notas if notas is not None else []

    @property
    def nombre(self):
        return self.__nombre

    @property
    def notas(self):
        return self.__notas

    @nombre.setter
    def nombre(self, nuevo_nombre):
        if not isinstance(nuevo_nombre, str):
            raise ValueError("El nombre debe ser un string")
        self.__nombre = nuevo_nombre

    @notas.setter
    def notas(self, nuevas_notas):
        if not isinstance(nuevas_notas, list):
            raise ValueError("Las notas nuevas deben ser una lista")
        self.__notas = nuevas_notas

    def agregar_nota(self, nota):
        if not isinstance(nota, (float, int)) or nota < 0:
            raise ValueError("La nueva nota debe ser un numero valido")
        self.__notas.append(nota)

    def promedio(self):
        if len(self.__notas) == 0:
            return 0
        return sum(self.__notas) / len(self.__notas)

    def __str__(self):
        return f"estudiante: {self.__nombre}, notas: {self.__notas}"


estudiante = Estudiante("Emmanuel")
estudiante.agregar_nota(8)
estudiante.agregar_nota(2.3)
print(estudiante.promedio())
print(estudiante)


# ------------------------------------------------------------------------------------
class Producto:
    def __init__(self, nombre: str, precio: float, stock: int):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def vender(self, cantidad: int):
        if cantidad <= 0:
            raise ValueError("La cantidad a vender debe ser un numero positivo")
        if cantidad > self.stock:
            raise ValueError(
                "La cantidad a vender es mayor que el stock disponible del producto"
            )
        self.stock -= cantidad

    def reponer(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad a reponer debe ser un numero positivo")
        self.stock += cantidad

    def __str__(self):
        return f"{self.nombre}: Precio {self.precio}€, Stock {self.stock}"


p1 = Producto("Manzanas", 1.5, 50)
p2 = Producto("Leche", 0.99, 20)
p3 = Producto("Pan", 1.2, 30)

print(p1.nombre, p1.precio, p1.stock)
print(p2.nombre, p2.precio, p2.stock)
print(p3.nombre, p3.precio, p3.stock)

p1.vender(10)
p2.vender(5)

print("\nDespués de vender:")
print(p1.nombre, p1.stock)
print(p2.nombre, p2.stock)

p1.reponer(20)
p3.reponer(10)

print("\nDespués de reponer:")
print(p1.nombre, p1.stock)
print(p3.nombre, p3.stock)


try:
    p2.vender(50)
except ValueError as e:
    print("\nError al vender:", e)

try:
    p3.reponer(-5)
except ValueError as e:
    print("Error al reponer:", e)
# ------------------------------------------------------------------------------------
