class Coche:

    ruedas = 4
    
    def __init__(self, color):
        self.color = color
        self.velocidad = 0
    
    @classmethod
    def numero_de_ruedas(cls):
        print(f"El coche tiene {cls.ruedas} ruedas")

    def acelerar(self, valor):
        self.velocidad += valor

        