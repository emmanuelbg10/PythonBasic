from archivo_multimedia import ArchivoMultimedia

class ArchivoImagen(ArchivoMultimedia):
    def __init__(self, nombre, tamaño, formato, resolucion):
        super().__init__(nombre, tamaño, formato, resolucion)
        self.resolucion = resolucion

    def reproducir(self):
        print(f"Reproduciendo imagen: {self.nombre} con resolucion: {self.resolucion}")

    def deteniendo(self):
        print(f"Deteniendo imagen: {self.nombre} con resolucion: {self.resolucion}")

    