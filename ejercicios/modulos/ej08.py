import random

caracteres = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
contraseña = ""

for i in range(8):
    caracter_aleatorio = random.choice(caracteres)
    contraseña += caracter_aleatorio

print(f"Contraseña generada: {contraseña}")
