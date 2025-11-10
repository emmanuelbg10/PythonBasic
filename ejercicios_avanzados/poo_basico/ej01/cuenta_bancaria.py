class CuentaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo

    def obtener_saldo(self):
        return self.__saldo

    def depositar(self, cantidad):
        self.__saldo += cantidad


    def retirar(self, cantidad):
        if self.__saldo < cantidad:
            print("No se ha podido retirar, saldo insuficiente")
            return
        self.__saldo -= cantidad
        print("Se ha retirado con exito el dinero de la cuenta")

    def __str__(self):
        return f"Tienes {self.__saldo}€ en tu cuenta"


cuenta = CuentaBancaria(1000)
cuenta.depositar(500)
print("Saldo:", cuenta.obtener_saldo())  

cuenta.retirar(2000) 
cuenta.retirar(1000) 
print(cuenta.obtener_saldo()) 
print(cuenta)
