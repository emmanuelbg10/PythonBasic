import os
from typing import List
import xml.etree.ElementTree as ET


class Libro:
    def __init__(self, titulo, autor, anio_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.anio_publicacion = anio_publicacion

    @classmethod
    def leer_libros(cls):
        libros = []
        ruta = os.path.dirname(__file__)
        archivo = os.path.join(ruta, "libros.xml")

        tree = ET.parse(archivo)
        root = tree.getroot()

        for libro in root.findall("libro"):
            titulo = libro.find("titulo").text
            autor = libro.find("autor").text
            anio_publicacion = libro.find("anio_publicacion").text

            libros.append(cls(titulo, autor, anio_publicacion))

        return libros


def guardar_libro(lista_libros: List[Libro]):
    ruta = os.path.dirname(__file__)
    archivo = os.path.join(ruta, "libros.xml")

    root = ET.Element("catalogo")

    for dato_libro in lista_libros:
        etiqueta_libro = ET.SubElement(root, "libro")

        titulo = ET.SubElement(etiqueta_libro, "titulo")
        titulo.text = dato_libro.titulo

        autor = ET.SubElement(etiqueta_libro, "autor")
        autor.text = dato_libro.autor

        anio_publicacion = ET.SubElement(etiqueta_libro, "anio_publicacion")
        anio_publicacion.text = str(dato_libro.anio_publicacion)

    tree = ET.ElementTree(root)

    tree.write(archivo, encoding="utf-8", xml_declaration=True)


libros = [
    Libro("Cien años de soledad", "Gabriel García Márquez", 1967),
    Libro("El nombre del viento", "Patrick Rothfuss", 2007),
    Libro("1984", "George Orwell", 1949),
]


guardar_libro(libros)
lista_libros: List[Libro] = Libro.leer_libros()
for libro in lista_libros:
    print(f"{libro.titulo}, {libro.autor}, {libro.anio_publicacion}")
