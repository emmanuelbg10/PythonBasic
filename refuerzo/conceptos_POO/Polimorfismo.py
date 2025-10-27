from Herencia import Perro, Gato

def hacer_hablar(animal):
    print(animal.hacer_sonido())

# Uso
hacer_hablar(Perro("Fido"))  # Guau
hacer_hablar(Gato("Misu"))   # Miau  