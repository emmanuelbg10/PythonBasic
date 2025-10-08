# GLOBAL (especifica valor devuelto por una funcion)

x = 10 # Esta es una variable global

def modificar_x():
    global x # Indicamos usar la variable global x
    x = x + 5 # Modificamos valor de variable global

print("Valor antes:", x) # Salida: Valor antes: 10
modificar_x()
print("Valor después:", x) # Salida: Valor después: 15