numbers = [1, 2, 3]
[x for x in numbers]
print("x" in globals() or "x" in locals()) # false

x = 10
print("x" in globals() or "x" in locals()) # true
