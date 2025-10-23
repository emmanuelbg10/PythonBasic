ciudades = {
    28001: "Madrid",
    25363: "Barcelona",
    41001: "Sevilla",
    29001: "Málaga",
    46001: "Valencia",
    50001: "Zaragoza"
}

print("Diccionario sin actualizar", ciudades)

codigo_a_eliminar = 41001

if codigo_a_eliminar in ciudades:
    del ciudades[codigo_a_eliminar]
    print(f"Se eliminó el código postal {codigo_a_eliminar}.")
    print("\nDiccionario actualizado: ",ciudades)
else:
    print("El código postal no existe en el diccionario.")

