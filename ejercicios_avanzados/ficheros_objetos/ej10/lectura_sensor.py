import struct
from typing import List
import os

ruta = os.path.dirname(__file__)
archivo = os.path.join(ruta, "lecturas.msgpack")


class LecturaSensor:
    def __init__(self, id_sensor, timestamp, valor):
        self.id_sensor = id_sensor
        self.timestamp = timestamp
        self.valor = valor

    def to_bytes(self):
        return struct.pack("iif", self.id_sensor, self.timestamp, self.valor)

    @classmethod
    def from_bytes(cls, data):
        id_sensor, timestamp, valor = struct.unpack("iif", data)
        return cls(id_sensor, timestamp, valor)

    @classmethod
    def guardar_lecturas(cls, lecturas: "List[LecturaSensor]"):
        with open(archivo, "wb") as file:
            for lectura in lecturas:
                file.write(lectura.to_bytes())

    @classmethod
    def leer_lecturas(cls):
        lecturas = []
        size = struct.calcsize("iif")
        with open(archivo, "rb") as file:
            bytes_leidos = file.read(size)
            while bytes_leidos:
                lecturas.append(cls.from_bytes(bytes_leidos))
                bytes_leidos = file.read(size)
        return lecturas


lecturas = [
    LecturaSensor(101, 1699999999, 23.5),
    LecturaSensor(102, 1700001234, 19.8),
    LecturaSensor(103, 1700005678, 21.2),
]

LecturaSensor.guardar_lecturas(lecturas)
lecturas_leidas: List[LecturaSensor] = LecturaSensor.leer_lecturas()

for lectura in lecturas_leidas:
    print(
        f"Sensor {lectura.id_sensor}, Timestamp {lectura.timestamp}, Valor {lectura.valor}"
    )
