def saludo_completo(nombre, saludo = "Hola"):
    return saludo + " " + nombre

nombre = "Emmanuel"
print(saludo_completo(nombre))
saludo = "Buenas"
print(saludo_completo(nombre, saludo))
