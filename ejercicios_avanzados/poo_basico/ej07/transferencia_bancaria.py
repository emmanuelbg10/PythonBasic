from metodo_pago import MetodoPago

class TransferenciaBancaria(MetodoPago):
    def __init__(self, cuenta_origen, cuenta_destino):
        self.cuenta_origen = cuenta_origen
        self.cuenta_destino = cuenta_destino


    def procesar_pago(self, monto):
        return f"Procesando pago de {monto:.2f}€ mediante transferencia desde {self.cuenta_origen} a {self.cuenta_destino}."