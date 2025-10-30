from deposito import Deposito
from pago import Pago
from transferencia import Transferencia
from datetime import datetime

class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo
    def aplicar_operacion(self, operacion):
        print(operacion.validar())

        if isinstance(operacion, Deposito):
            self.saldo += operacion.monto

        elif isinstance(operacion, Pago) or isinstance(operacion, Transferencia):
            if operacion.monto > self.saldo:
                print("No hay suficiente saldo")
                return
            
            self.saldo -= operacion.monto

        else:
            print("Operación desconocida")
            return

        print(operacion.ejecutar())
        print(f"Saldo actual: {self.saldo}€\n")
    

cuenta = CuentaBancaria("Juan", 1000)

dep = Deposito(500, datetime.now())
pago = Pago(200, datetime.now())
trans = Transferencia(300, datetime.now())

cuenta.aplicar_operacion(dep)     
cuenta.aplicar_operacion(pago)   
cuenta.aplicar_operacion(trans)  

