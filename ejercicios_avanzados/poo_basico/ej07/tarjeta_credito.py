from metodo_pago import MetodoPago

class TarjetaCredito(MetodoPago):
    def __init__(self, numero_tarjeta, titular, cvv):
        self.numero_tarjeta = numero_tarjeta
        self.titular = titular
        self.cvv = cvv

    def procesar_pago(self, monto):
        return f"Procesando pago de {monto:.2f}€ con tarjeta de crédito de {self.titular}."