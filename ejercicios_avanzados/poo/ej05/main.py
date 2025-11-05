from tren import Tren
from tranvia import Tranvia
from autobus import Autobus
from red_transporte import RedTransporte

red = RedTransporte()

red.agregar_vehiculo(Tren(200, 160, ["tarjeta"], "T1"))
red.agregar_vehiculo(Tranvia(100, 60, ["efectivo", "tarjeta"], "TR1"))
red.agregar_vehiculo(Autobus(50, 90, ["efectivo"], "B1"))


print(red.vehiculos[0].sistema_cobro("tarjeta", 1000))
print(red.vehiculos[1].sistema_cobro("efectivo", 20))
print(red.vehiculos[2].sistema_cobro("efectivo", 20))

red.iniciar_todos_viajes()
