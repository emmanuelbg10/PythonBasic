from perro import Perro
from gato import Gato
from pajaro import Pajaro
from animal import Animal
from typing import List

def main():
    animales = [
        Perro("Lukas", 7, "Labrador"),
        Gato("Michino", 12, "Siames"),
        Pajaro("Coco", 9, "Alejandrina")
    ]

    def hacer_sonar_todos(lista_animales: List[Animal]):
        for animal in lista_animales:
            print(animal.hacer_sonido())
    hacer_sonar_todos(animales)
    

if __name__ == "__main__":
    main()