import os
from typing import List
import msgpack

ruta = os.path.dirname(__file__)
archivo = os.path.join(ruta, "jugadores.msgpack")


class Jugador:
    def __init__(self, nombre, puntuacion):
        self.nombre = nombre
        self.puntuacion = puntuacion

    @classmethod
    def guardar_jugadores(cls, jugadores: "List[Jugador]"):
        dict_jugadores = [
            {"nombre": jugador.nombre, "puntuacion": jugador.puntuacion}
            for jugador in jugadores
        ]

        with open(archivo, "wb") as file:
            packed = msgpack.packb(dict_jugadores)
            file.write(packed)

    @classmethod
    def leer_jugadores(cls):

        with open(archivo, "rb") as file:
            jugadores_leidos = msgpack.unpack(file, raw=False)

            jugadores = [
                cls(jugador["nombre"], jugador["puntuacion"])
                for jugador in jugadores_leidos
            ]

            return jugadores


lista_jugadores = [
    Jugador("Messi", 97),
    Jugador("Cristiano", 95),
    Jugador("Mbappé", 92),
]

Jugador.guardar_jugadores(lista_jugadores)
jugadores: List[Jugador] = Jugador.leer_jugadores()

for jugador in jugadores:
    print(f"{jugador.nombre}, {jugador.puntuacion}")
