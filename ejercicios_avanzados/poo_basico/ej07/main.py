from carrito import Carrito
from tarjeta_credito import TarjetaCredito
from transferencia_bancaria import TransferenciaBancaria
from efectivo import Efectivo

def main():
    carrito = Carrito()
    carrito.agregar_item("Camisa", 25.50)
    carrito.agregar_item("Pantalón", 40.00)
    carrito.agregar_item("Zapatos", 60.00)

    print("Items en el carrito:")
    carrito.mostrar_items()

    tarjeta = TarjetaCredito("1234-5678-9012-3456", "Ana", "123")
    transferencia = TransferenciaBancaria("ES123456789", "ES987654321")
    efectivo = Efectivo()

    print("\nPagando con tarjeta de crédito:")
    carrito.procesar_pago(tarjeta)

    print("\nPagando con transferencia bancaria:")
    carrito.procesar_pago(transferencia)

    print("\nPagando en efectivo:")
    carrito.procesar_pago(efectivo)


if __name__ == "__main__":
    main()
