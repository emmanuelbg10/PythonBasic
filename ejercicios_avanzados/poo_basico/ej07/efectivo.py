from metodo_pago import MetodoPago

class Efectivo(MetodoPago):
    def procesar_pago(self, monto):
        return f"Procesando pago de {monto:.2f}€ en efectivo."