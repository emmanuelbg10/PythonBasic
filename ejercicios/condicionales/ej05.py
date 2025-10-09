num = int(input("Escribe un numero del 1 al 7: "))
week = {
    1: "Lunes",
    2: "Martes",
    3: "Miercoles",
    4: "Jueves",
    5: "Viernes",
    6: "Sabado",
    7: "Domingo"
}.get(num, "Error, vuelva a intentarlo")

print(week)