from archivo_multimedia import ArchivoMultimedia

class ArchivoVideo(ArchivoMultimedia):
    def __init__(self, nombre, tamaño, formato, duracion, resolucion):
        super().__init__(nombre, tamaño, formato)
        self.duracion = duracion
        self.resolucion = resolucion

    def reproducir(self):
        print(f"Reproduciendo video: {self.nombre}, duración: {self.duracion}, resolución: {self.resolucion}")

    def deteniendo(self):
        print(f"Deteniendo video: {self.nombre}, duración: {self.duracion}, resolución: {self.resolucion}")
