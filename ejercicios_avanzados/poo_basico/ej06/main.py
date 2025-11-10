from forma import Forma
from rectangulo import Rectangulo
from circulo import Circulo
from triangulo import Triangulo
from typing import List

def calcular_area_total(lista_formas: List[Forma]) -> float:
    total = 0
    for forma in lista_formas:
        area = forma.calcular_area()
        print(f"{forma.__class__.__name__} área: {area:.2f}")
        total += area
    return total

def main():
    rect = Rectangulo(5, 10)
    circ = Circulo(3)
    tri = Triangulo(4, 6)

    formas = [rect, circ, tri]

    total = calcular_area_total(formas)
    print(f"\nÁrea Total: {total:.2f}")

if __name__ == "__main__":
    main()
