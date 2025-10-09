print("Determinar los años bisiestos")

year = int(input("Escribe un año: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Tu año es bisiesto")
else:
    print("Tu año no es bisiesto")
