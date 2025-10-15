num = int(input("Introduce un número entero: "))

# guardamos el signo y trabajamos con el valor absoluto
if num < 0:
    signo = "-"
    n = -num
else:
    signo = ""
    n = num

# caso especial para el 0
if n == 0:
    binario = "0"
else:
    binario = ""
    while n > 0:
        residuo = n % 2            # Tomamos el residuo de dividir entre 2
        binario = str(residuo) + binario # Lo agregamos al inicio
        n = n // 2                 # Dividimos entre 2 para el siguiente paso

# Mostramos el resultado con el signo
print(f"El número {num} en binario es: {signo}{binario}")