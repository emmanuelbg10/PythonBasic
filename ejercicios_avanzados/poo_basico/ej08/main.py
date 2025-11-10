from televisor import Televisor
from computadora import Computadora
from smartphone import Smartphone
from dispositivo import Dispositivo
from typing import List

def main():
    dispositivos = [
        Televisor(),
        Computadora(),
        Smartphone()
    ]


    def cambiar_estado(lista_dispositivos: List[Dispositivo], accion):

        if accion != "encendido" and accion != "apagado":
            return "No elegiste una accion valida"
        
        for dispositivo in lista_dispositivos:
            if accion == "encendido":
                dispositivo.encender()
            else:
                dispositivo.apagar()

    cambiar_estado(dispositivos, "apagado")


if __name__ == "__main__":
    main()


