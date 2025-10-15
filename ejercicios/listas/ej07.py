lista = [7, 9, 2, 5, 4]
promedio = sum(lista) / len(lista)

mayores_al_promedio = list(filter(lambda x: x > promedio, lista))

print(f"La nota promedio es: {promedio}")

print(f"Los numeros mayores al promedio son: {mayores_al_promedio}")
