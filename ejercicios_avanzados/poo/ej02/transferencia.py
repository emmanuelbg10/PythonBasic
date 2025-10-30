from operacion_financiera import OperacionFinanciera

class Transferencia(OperacionFinanciera):
    def validar(self):
        if self.monto <= 0:
            return "La transferencia debe ser mayor a 0"
        if self.monto > 5000:
            return "Transferencia requiere revisión especial"
        return "Transferencia validada"

    def ejecutar(self):
        return f"Transferencia de {self.monto} ejecutada el {self.fecha}"