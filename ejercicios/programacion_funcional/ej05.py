lista = ["hola", "buenas", "que", "tal"]


print(f"Lista normal: {lista}")

lista_mayuscula = list(map(lambda x: x.upper(), lista ))


print(f"Lista mayuscula: {lista_mayuscula}")