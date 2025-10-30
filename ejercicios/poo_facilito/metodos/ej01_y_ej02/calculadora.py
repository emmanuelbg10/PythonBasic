class Calculadora:

    @classmethod
    def sumar(cls, num1, num2):
        resultado = num1 + num2
        cls.mostrar_mensaje()
        return resultado

    @classmethod
    def restar(cls, num1, num2):
        resultado = num1 - num2
        cls.mostrar_mensaje()
        return resultado
    
    @staticmethod
    def mostrar_mensaje():
        print("Cálculo realizado")

print(Calculadora.sumar(5, 4))
print(Calculadora.restar(3, 2))

