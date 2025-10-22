import statistics

numeros = [10, 15, 20, 25, 30, 35, 40]

media = statistics.mean(numeros)

mediana = statistics.median(numeros)

desviacion = statistics.stdev(numeros) # desviacion estandar

print(f"Lista de números: {numeros}")
print(f"Media: {media}")
print(f"Mediana: {mediana}")
print(f"Desviación estándar: {desviacion}")
