class CuentaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo

    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self, nuevo_saldo):
        if nuevo_saldo >= 0:
            self.__saldo = nuevo_saldo

cuenta1 = CuentaBancaria(2000)

print("Saldo:", cuenta1.saldo)


cuenta1.saldo = 1

print("Nuevo saldo:", cuenta1.saldo)

cuenta1.saldo = -2

print("No hay cambios:", cuenta1.saldo)

print("No hay cambios porque el saldo no puede ser nunca menor a 0")
