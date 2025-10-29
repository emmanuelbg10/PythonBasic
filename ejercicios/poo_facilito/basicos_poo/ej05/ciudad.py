class Ciudad:
    def __init__(self, nombre, poblacion):
        self.nombre = nombre
        self.poblacion = poblacion

ciudad = Ciudad("Madrid", 999999)

print(f"La ciudad {ciudad.nombre} tiene esta poblacion: {ciudad.poblacion}")
