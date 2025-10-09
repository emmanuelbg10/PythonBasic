print("Solicitando contraseñas")
password1 = input("Escribe una contraseña: ")
password2 = input("Escribe otra contraseña: ")

if len(password1) < 8 or len(password2) < 8:
    print("Las contraseñas tienen que tener 8 caracteres o mas")
elif password1 == password2:
    print("Las contraseñas son iguales")