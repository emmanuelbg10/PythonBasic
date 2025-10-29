class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

milibro = Libro("El Quijote", "Cervantes")

print(f"El libro tiene el titulo: {milibro.titulo} y el autor del libro es: {milibro.autor}")