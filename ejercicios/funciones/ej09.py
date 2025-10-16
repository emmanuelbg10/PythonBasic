def promedio(*args):
    # Verificar que se hayan pasado números
    if len(args) == 0:
        return 0  

    return sum(args) / len(args)

print(promedio(2, 4, 6, 8))  
print(promedio(10, 20))   
