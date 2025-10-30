class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        return f"el animal {self.nombre} está hablando"

if __name__ == "__main__":
    animal = Animal("pajaro") 
    print(animal.hablar())