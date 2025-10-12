print("Secuencia fibonacci: ")
def fibonacci(num):
    if num == 0:
        return [0]
    elif num == 1:
        return [0, 1]

    fib_sequence = [0, 1]
    a, b = 0, 1

    for _ in range(2, num):
        c = a + b
        print(f"  {a} + {b} = {c}")  
        fib_sequence.append(c)
        a, b = b, c

    return fib_sequence

fibonacci_numbers = fibonacci(15)
print("Serie completa:", ', '.join(map(str, fibonacci_numbers)))
