print("Determinador de vocales, consonantes, un dígito o un símbolo especial")

char = input("Escribe un solo carácter: ")

if len(char) != 1:
    print("Por favor, ingresa solo un carácter.")
elif char.isdigit():
    print("Es un dígito")
elif char.isalpha(): #verifica si todos los caracteres son letras y que no esté vacio
    if char.lower() in "aeiou": # importante aprender, in es como un contain
        print("Es una vocal")
    else:
        print("Es una consonante")
else:
    print("Es un símbolo especial")
