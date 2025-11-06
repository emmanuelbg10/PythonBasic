from archivo_multimedia import ArchivoMultimedia

class ArchivoAudio(ArchivoMultimedia):
    def __init__(self, nombre, tamaño, formato, duracion, artista):
        super().__init__(nombre, tamaño, formato)
        self.duracion = duracion
        self.artista = artista

    def reproducir(self):
        print(f"Reproduciendo audio: {self.nombre} de {self.artista} con duración de {self.duracion}")

    def deteniendo(self):
        print(f"Deteniendo audio: {self.nombre} de {self.artista} con duración de {self.duracion}")
