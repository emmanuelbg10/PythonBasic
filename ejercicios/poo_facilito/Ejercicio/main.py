from coche import Coche

Coche.numero_de_ruedas()


coche1 = Coche("Azul")

print("Velocidad inicial del coche1", coche1.velocidad)

coche1.acelerar(50)

print("Velocidad actual del coche1", coche1.velocidad)

coche1.acelerar(20)

print("Velocidad actual del coche1", coche1.velocidad)


coche2 = Coche("Rojo")

print("Velocidad inicial del coche2", coche2.velocidad)

coche2.acelerar(10)

print("Velocidad actual del coche2", coche2.velocidad)

coche2.acelerar(15)

print("Velocidad actual del coche2", coche2.velocidad)

print(f"El coche 1 tiene este color {coche1.color} y el coche 2 tiene este color {coche2.color}")

