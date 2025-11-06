class ArchivoMultimedia:
    def __init__(self, nombre, tamaño, formato):
        self.nombre = nombre
        self.tamaño = tamaño
        self.formato = formato
        pass

    def reproducir(self):
        print(f"Reproduciendo el archivo {self.nombre}.{self.formato}")

    def deteniendo(self):
        print(f"Deteniendo el archivo {self.nombre}.{self.formato}")

    def __str__(self):
        return f"Nombre: {self.nombre}\nTamaño: {self.tamaño} MB\nFormato: {self.formato}"
    