from archivo_multimedia import ArchivoMultimedia
from archivo_audio import ArchivoAudio
from archivo_imagen import ArchivoImagen
from archivo_video import ArchivoVideo


class Reproductor:
    def __init__(self, lista_archivos=None):
        self.lista_archivos = lista_archivos if lista_archivos is not None else []

    def agregar(self, archivo: ArchivoMultimedia):
        """Agrega un archivo multimedia a la lista."""
        self.lista_archivos.append(archivo)
        print(f"Archivo '{archivo.nombre}' agregado correctamente.")

    def eliminar(self, nombre):
        """Elimina un archivo por su nombre."""
        for archivo in self.lista_archivos:
            if archivo.nombre == nombre:
                self.lista_archivos.remove(archivo)
                print(f"Archivo '{nombre}' eliminado correctamente.")
                return
        print(f"Archivo '{nombre}' no se encuentra en la lista.")

    def reproducir_archivos(self):
        """Reproduce todos los archivos de la lista."""
        for archivo in self.lista_archivos:
            print(archivo.reproducir())

    def detener_archivos(self):
        """Detiene la reproducción de todos los archivos."""
        for archivo in self.lista_archivos:
            print(archivo.deteniendo())


audio1 = ArchivoAudio("cancion_rock.mp3", 5.6, "MP3", "00:03:45", "Shawn James")
video1 = ArchivoVideo("documental_naturaleza.mp4", 850.5, "MP4", "00:45:30", "1920x1080")
imagen1 = ArchivoImagen("paisaje_montaña.jpg", 2.4, "JPG", "3840x2160")

reproductor = Reproductor([audio1, video1])
reproductor.agregar(imagen1)

reproductor.reproducir_archivos()
reproductor.detener_archivos()
