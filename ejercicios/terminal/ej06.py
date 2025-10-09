price = float(input("Dame un precio sin IVA: "))
iva = float(input("Dime el IVA (%): "))

iva_decimal = iva / 100

monto_iva = price * iva_decimal

price_with_iva = price + monto_iva

print(f"El IVA es: {monto_iva}")
print(f"El precio con IVA es: {price_with_iva}")
