# Solicita un número entre 1 y 12 y muestra el nombre del mes 
# correspondiente. 
# Si el número está fuera de rango, muestra un mensaje de error.

num = int(input("Escribe un número del 1 al 12: "))

mes = {
    1: "Enero", 2: "Febrero", 3: "Marzo", 
    4: "Abril", 5: "Mayo", 6: "Junio", 
    7: "Julio", 8: "Agosto", 9: "Septiembre", 
    10: "Octubre", 11: "Noviembre", 12: "Diciembre"
}.get(num, "Número fuera de rango")

print(mes)
