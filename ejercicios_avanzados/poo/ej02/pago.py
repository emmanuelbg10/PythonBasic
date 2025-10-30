from operacion_financiera import OperacionFinanciera

class Pago(OperacionFinanciera):
    def validar(self):
        if self.monto > 1000:
            return "Pago requiere autorización"
        return "Pago validado"

    def ejecutar(self):
        return f"Pago de {self.monto} ejecutado el {self.fecha}"