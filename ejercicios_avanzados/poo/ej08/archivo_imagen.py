from archivo_multimedia import ArchivoMultimedia

class ArchivoImagen(ArchivoMultimedia):
    def __init__(self, nombre, tamaño, formato, resolucion):
        super().__init__(nombre, tamaño, formato)
        self.resolucion = resolucion

    def reproducir(self):
        print(f"Mostrando imagen: {self.nombre} con resolución {self.resolucion}")

    def deteniendo(self):
        print(f"Cerrando imagen: {self.nombre} con resolución {self.resolucion}")
