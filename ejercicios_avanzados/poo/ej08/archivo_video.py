from archivo_multimedia import ArchivoMultimedia

class ArchivoVideo(ArchivoMultimedia):
    def __init__(self, nombre, tamaño, formato, duracion, resolucion):
        super().__init__(nombre, tamaño, formato, duracion, resolucion)
        self.duracion = duracion
        self.resolucion = resolucion

    def reproducir(self):
        print(f"Reproduciendo video: {self.nombre}, con duracion: {self.duracion} y con resolucion: {self.resolucion}")

    def deteniendo(self):
        print(f"Deteniendo video: {self.nombre}, con duracion: {self.duracion} y con resolucion: {self.resolucion}")

    