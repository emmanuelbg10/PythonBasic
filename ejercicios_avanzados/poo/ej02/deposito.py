from operacion_financiera import OperacionFinanciera

class Deposito(OperacionFinanciera):
    def validar(self):
        if self.monto <= 0:
            return "El depósito debe ser mayor a 0"
        return "Depósito validado"

    def ejecutar(self):
        return f"Depósito de {self.monto} ejecutado el {self.fecha}"