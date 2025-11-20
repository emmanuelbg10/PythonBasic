import os
from typing import List
import xml.etree.ElementTree as ET


class Contacto:
    def __init__(self, nombre, telefono, email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email

    @classmethod
    def leer_contactos(cls):
        contactos = []
        ruta = os.path.dirname(__file__)
        archivo = os.path.join(ruta, "contactos.xml")

        tree = ET.parse(archivo)
        root = tree.getroot()

        print("Nombre de todos los contactos:")
        for contacto in root.findall("contacto"):

            nombre = contacto.find("nombre").text
            print(nombre)

            telefono = contacto.find("telefono").text

            email = contacto.find("email").text

            contactos.append(cls(nombre, telefono, email))

        return contactos


def guardar_contactos(lista_contactos: List[Contacto]):
    ruta = os.path.dirname(__file__)
    archivo = os.path.join(ruta, "contactos.xml")

    root = ET.Element("contactos")

    for datos_contacto in lista_contactos:
        contacto = ET.SubElement(root, "contacto")

        nombre = ET.SubElement(contacto, "nombre")
        nombre.text = datos_contacto.nombre

        telefono = ET.SubElement(contacto, "telefono")
        telefono.text = datos_contacto.telefono

        email = ET.SubElement(contacto, "email")
        email.text = datos_contacto.email

        tree = ET.ElementTree(root)

        tree.write(archivo, encoding="utf-8", xml_declaration=True)


lista_contactos = [
    Contacto("Ana Martínez", "600123456", "ana.martinez@email.com"),
    Contacto("Juan Pérez", "611987654", "juan.perez@email.com"),
    Contacto("Lucía Gómez", "622555888", "lucia.gomez@email.com"),
]

guardar_contactos(lista_contactos)

contactos: List[Contacto] = Contacto.leer_contactos()

print("\nInformacion de Contactos:")
for contacto in contactos:
    print(f"{contacto.nombre}, {contacto.telefono}, {contacto.email}")
