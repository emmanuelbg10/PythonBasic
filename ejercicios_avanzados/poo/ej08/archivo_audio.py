from archivo_multimedia import ArchivoMultimedia

class ArchivoAudio(ArchivoMultimedia):
    def __init__(self, nombre, tamaño, formato, duracion, artista):
        super().__init__(nombre, tamaño, formato, duracion, artista)
        self.duracion = duracion
        self.artista = artista


    def reproducir(self):
        print(f"Reproduciendo audio: {self.nombre} de {self.artista} con duracion de: {self.duracion} de audio")

    def deteniendo(self):
        print(f"Deteniendo iaudio: {self.nombre} de {self.artista} con duracion de: {self.duracion} de audio")

    