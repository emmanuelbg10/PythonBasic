num1 = int(input("Escribe un numero: "))
num2 = int(input("Escribe otro numero: "))
if num1 > num2:
    print(f"El numero mas grande es:  {num1}")
elif num2 > num1:
    print(f"El numero mas grande es: {num2}")
else: 
    print("Los dos numeros son iguales")