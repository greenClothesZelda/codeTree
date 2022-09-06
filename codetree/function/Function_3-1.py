def swap(a, b):
    b, a = a, b
    return a, b
a, b = swap(*input().split())
print(f"{a} {b}")