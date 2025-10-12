while True:
    num = input("Escribe un número y te diré cuántos dígitos tiene: ")

    # validacion de si es un numero
    try:
        float(num)
    except ValueError:
        print("Esto no es un número, vuelve a intentarlo")
        continue # si no es un digito se repite el bucle

    # Eliminamos el signo negativo (si tenia lo quita y si no, no hace nada)
    num_sin_signo = num.lstrip("-")

    # Separamos parte entera y decimal
    if "." in num_sin_signo:
        entero, decimal = num_sin_signo.split(".")
        print(f"Parte entera: {len(entero)} dígito(s), Parte decimal: {len(decimal)} dígito(s)")
    else:
        print(f"Parte entera: {len(num_sin_signo)} dígito(s), Parte decimal: 0 dígito(s)")

    break
