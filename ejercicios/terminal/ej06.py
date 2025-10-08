price = float(input("Dame un precio sin IVA: "))
iva = float(input("Dime el IVA (%): "))

price_with_iva = price * (1 + iva / 100)

print(f"El precio con IVA es: {price_with_iva}")
