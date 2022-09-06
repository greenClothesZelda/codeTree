product = 1

def f(n):
    for i in range(1, n + 1):
        product *= i

f(5)

print(product)

