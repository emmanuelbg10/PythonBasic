class Animal:
    def __init__(self, nombre, especie, edad):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad

    def emitir_sonido(self):
        print("Este animal hace un sonido.")

    def alimentarse(self):
        return f"{self.nombre} está comiendo."

    def dormir(self):
        return f"{self.nombre} está durmiendo."

    def __str__(self):
        return f"{self.especie} llamado {self.nombre}, de {self.edad} años."
