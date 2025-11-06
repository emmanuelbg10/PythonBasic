from forma import Forma
from typing import List
from rectangulo import Rectangulo
from circulo import Circulo
from triangulo import Triangulo

class GrupoDeFormas(Forma):
    def __init__(self, nombre):
        self.formas = []
        self.nombre = nombre

    def agregar(self, forma: Forma):
        self.formas.append(forma)

    def eliminar(self, forma: Forma):
        self.formas.remove(forma)

    def dibujar(self):
        cabecera = f"GrupoDeFormas '{self.nombre}': comenzando a dibujar {len(self.formas)} elemento(s)"
        print(cabecera)
        for i, forma in enumerate(self.formas, start=1):
            print(f"Elemento {i} de {len(self.formas)} en '{self.nombre}':")
            forma.dibujar()
        print(f"GrupoDeFormas '{self.nombre}': terminado")

def dibujar_escena(formas: List[Forma]) -> None:

    print("Dibujando escena:")
    for i, forma in enumerate(formas, start=1):
        print(f"\nForma {i}:")
        forma.dibujar()

    print("Fin de la escena")


r1 = Rectangulo("azul")
c1 = Circulo("rojo")
t1 = Triangulo("verde")
t2 = Triangulo("morado")

grupo = GrupoDeFormas(nombre="Grupo de Triangulos")
grupo.agregar(t1)
grupo.agregar(t2)
 
escena = [r1, grupo, c1]

dibujar_escena(escena)
