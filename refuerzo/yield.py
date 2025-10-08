def contador(max):
    n = 0
    while n < max:
        yield n
        n = n + 1
mycont = contador(3)

for i in mycont:
    print(f"valor leido del iterador={i}")