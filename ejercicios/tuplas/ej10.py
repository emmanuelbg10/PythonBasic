productos = [("manzana", 20), ("pera", 60), ("agua", 10), ("mandarina", 70)]

a = list(filter(lambda x: x[1] > 50, productos))

print(a)
