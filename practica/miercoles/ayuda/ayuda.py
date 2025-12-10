import os
import json
import msgpack
import struct
import xml.etree.ElementTree as ET


def ruta(nombre_archivo):
    carpeta = os.path.dirname(__file__)
    return os.path.join(carpeta, nombre_archivo)


# ============================================================
#                ARCHIVOS DE TEXTO (TXT)
# ============================================================


def guardar_txt(nombre, texto):
    with open(ruta(nombre), "w", encoding="utf-8") as file:
        file.write(texto)


def leer_txt(nombre):
    with open(ruta(nombre), "r", encoding="utf-8") as file:
        return file.read()


# ============================================================
#                       ARCHIVOS JSON
# ============================================================


def guardar_json(nombre, datos):
    with open(ruta(nombre), "w", encoding="utf-8") as file:
        json.dump(datos, file, indent=4, ensure_ascii=False)


def leer_json(nombre):
    with open(ruta(nombre), "r", encoding="utf-8") as file:
        return json.load(file)


# ============================================================
#                       ARCHIVOS XML
# ============================================================


def guardar_xml(nombre, nombre_raiz, datos):
    """
    Guarda un diccionario en un XML sencillo.
    - nombre_raiz -> nombre del nodo raíz
    - datos -> diccionario
    """
    root = ET.Element(nombre_raiz)

    for clave, valor in datos.items():

        elemento = ET.SubElement(root, clave)

        if isinstance(valor, dict):
            for subclave, subvalor in valor.items():
                hijo = ET.SubElement(elemento, subclave)
                hijo.text = str(subvalor)
        else:
            elemento.text = str(valor)

    tree = ET.ElementTree(root)
    tree.write(ruta(nombre), encoding="utf-8", xml_declaration=True)


def leer_xml(nombre):
    tree = ET.parse(ruta(nombre))
    root = tree.getroot()

    datos = {}

    for elem in root:
        if len(elem) == 0:
            datos[elem.tag] = elem.text
        else:
            sub_dict = {}
            for sub in elem:
                sub_dict[sub.tag] = sub.text
            datos[elem.tag] = sub_dict

    return datos


# ============================================================
#                    ARCHIVOS MSGPACK (BINARIO)
# ============================================================


def guardar_msgpack(nombre, datos):
    with open(ruta(nombre), "wb") as file:
        file.write(msgpack.packb(datos, use_bin_type=True))


def leer_msgpack(nombre):
    with open(ruta(nombre), "rb") as file:
        return msgpack.unpackb(file.read(), raw=False)


# ============================================================
#                 ARCHIVOS BINARIOS CON STRUCT
# ============================================================

"""
STRUCT sirve para guardar valores con un formato fijo.
Ejemplo: guardar un número entero y un float.
Formato:
    'i' -> entero
    'f' -> float
    'd' -> double
    's' -> string en bytes
"""


def guardar_struct(nombre, formato, *valores):
    """
    ejemplo uso: guardar_struct("datos.bin", "if", 25, 3.14)
    """
    with open(ruta(nombre), "wb") as file:
        empaquetado = struct.pack(formato, *valores)
        file.write(empaquetado)


def leer_struct(nombre, formato):
    with open(ruta(nombre), "rb") as file:
        contenido = file.read()
        return struct.unpack(formato, contenido)


# ============================================================
#                           PRUEBAS
# ============================================================

if __name__ == "__main__":

    guardar_txt("archivo.txt", "Hola mundo")
    print(leer_txt("archivo.txt"))

    guardar_json("datos.json", {"nombre": "Emmanuel"})
    print(leer_json("datos.json"))

    guardar_xml("datos.xml", "Personas", {"Marco": {"edad": 40}})
    print(leer_xml("datos.xml"))

    guardar_msgpack("datos.msgpack", {"nombre": "Marco", "edad": 40})
    print(leer_msgpack("datos.msgpack"))

    guardar_struct("datos.bin", "if", 23, 9.5)
    print(leer_struct("datos.bin", "if"))
