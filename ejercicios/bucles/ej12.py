num = int(input("Introduce un número: "))

if num < 2:
    print(f"{num} no es primo")
else:
    primo = True
    for i in range(2, num):
        if num % i == 0:
            primo = False
            break

    if primo:
        print(f"{num} es primo")
    else:
        print(f"{num} no es primo")
