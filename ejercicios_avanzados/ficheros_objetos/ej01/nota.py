import os


class Nota:
    def __init__(self, titulo, contenido):
        self.titulo = titulo
        self.contenido = contenido

    @classmethod
    def leer_desde_archivo(cls):
        notas = []
        ruta_actual = os.path.dirname(__file__)
        archivo = os.path.join(ruta_actual, "notas.txt")
        try:
            with open(archivo, "r") as file:
                for line in file.readlines():
                    titulo, contenido = line.split(" - ", 1)
                    nota = cls(titulo.strip(), contenido.strip())
                    notas.append(nota)
        except OSError:
            print("No fue posible leer el archivo")

        return notas


nota1 = Nota("Compras", "Comprar leche, pan y cereales")
nota2 = Nota("Videojuegos", "Jugar Cyberpunk 2077")

ruta_actual = os.path.dirname(__file__)
archivo = os.path.join(ruta_actual, "notas.txt")

try:
    with open(archivo, "w") as file:
        for nota in nota1, nota2:
            file.write(f"{nota.titulo} - {nota.contenido}\n")
except OSError:
    print("No fue posible crear el archivo")


notas = Nota.leer_desde_archivo()
for nota in notas:
    print(f"{nota.titulo}: {nota.contenido}")
