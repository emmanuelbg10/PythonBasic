# ----------------------------------------------------------------------------------
print("PASO1: devuelve max, min y promedio")


def max_min_promedio(*args):
    return {"max": max(args), "min": min(args), "promedio": sum(args) / len(args)}


print(max_min_promedio(1, 2, 6, 8, 0, 3))

# ----------------------------------------------------------------------------------
print("\nPASO2: Nombres de personas mayores de edad")


def mayores(**kwargs):
    return [nombre for nombre, edad in kwargs.items() if edad > 18]


print(mayores(Emmanuel=20, Juanito=10, Joel=30))
# ----------------------------------------------------------------------------------
