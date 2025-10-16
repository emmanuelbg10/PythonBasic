def factorial(n):
    # Caso base: el factorial de 0 o 1 es 1
    if n == 0 or n == 1:
        return 1
    else:
        # Caso recursivo: n * factorial de (n-1)
        return n * factorial(n - 1)

# Ejemplo de uso
numero = 5
print(f"El factorial de {numero} es {factorial(numero)}")
