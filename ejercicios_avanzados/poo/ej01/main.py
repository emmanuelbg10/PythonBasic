from barco import Barco
from dron import Dron

b = Barco("Neptuno", "gasolina", 100)
print(b.iniciar_sistema_navegacion())
print(b.mover())
print(b.detener())
print(f"Autonomía del barco: {b.calcular_autonomia()} km")

d = Dron("Aquila", "electrico", 50)
print(d.iniciar_sistema_navegacion())
print(d.mover())
print(d.detener())
print(f"Autonomía del dron: {d.calcular_autonomia()} km")
