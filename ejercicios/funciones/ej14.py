def convertir_grados(c, x = "F"):
    if x == "F":
        return f"Celsius: {c}, Fahrenheit: {c * 9 / 5 + 32}" 
    elif x == "K":
        return f"Celsius: {c}, Kelvin: {c + 273.15}" 
    else:
        return "Tipo de grado no valido"
    
print(convertir_grados(2, "K"))

