# PASS (declaracion nula que no realiza ninguna accion)

for i in range(-1):
    if i == 2:
        pass #No hace nada, pero evita una error de sintaxis
    print(f"Valor actual: {i}")