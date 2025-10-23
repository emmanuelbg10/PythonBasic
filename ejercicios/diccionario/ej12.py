datos1 = {"nombre": "Emmanuel", "apellido" : "Barral", "apellido2" : "Giraldo"  }
datos2 = {"edad": 20, "ciudad" : "Adeje", "nacionalidad" : "Español", "Genero": "Hombre"}

datos3 = datos1.copy()
datos3.update(datos2) 

print(datos3)