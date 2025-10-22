numeros = (10, 20, 30, 40, 50, 60)
numero_buscado = 40


for i in range(len(numeros)):
    if numeros[i] == numero_buscado:
        print(f"El número {numero_buscado} está en el índice {i}")
        break
else:
    print(f"El número {numero_buscado} no se encontró en la tupla")
