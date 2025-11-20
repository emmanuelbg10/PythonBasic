import os
from typing import List
import json


class Usuario:
    def __init__(self, nombre, configuracion):
        self.nombre = nombre
        self.configuracion = configuracion

    @classmethod
    def leer_usuarios(cls):
        usuarios = []

        ruta = os.path.dirname(__file__)
        archivo = os.path.join(ruta, "usuarios.json")

        with open(archivo, encoding="utf-8") as file:
            usuarios_leidos = json.load(file)

            for usuario in usuarios_leidos:
                usuarios.append(cls(usuario["nombre"], usuario["configuracion"]))

            return usuarios


def guardar_usuarios(dict_usuarios):
    ruta = os.path.dirname(__file__)
    archivo = os.path.join(ruta, "usuarios.json")

    with open(archivo, "w", encoding="utf-8") as file:
        json.dump(dict_usuarios, file, ensure_ascii=False, indent=4)


lista_usuarios = [
    Usuario("Ana", {"tema": "oscuro", "notificaciones": True}),
    Usuario("Luis", {"tema": "claro", "notificaciones": False}),
    Usuario("Marta", {"tema": "oscuro", "notificaciones": False}),
]

dict_usuarios = [
    {"nombre": usuario.nombre, "configuracion": usuario.configuracion}
    for usuario in lista_usuarios
]

guardar_usuarios(dict_usuarios)

usuarios: List[Usuario] = Usuario.leer_usuarios()

for i, usuario in enumerate(usuarios, start=1):
    print(f"Usuario{i}: {usuario.nombre}\nConfiguracion: {usuario.configuracion}\n")
