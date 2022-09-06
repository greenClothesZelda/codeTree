n = int(input())

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

def get(x, y):
    if x < 0 or y < 0:
        return -100
    if x >= len(arr) or y >= len(arr[0]):
        return -100
    return arr[x][y]

def make(x, y):
    _sum = 0
    for _ in range(3):
        _sum += get(x, y)

        y += 1

    return _sum

max_val = 0

for i in range(n):
    for j in range(n-2):
        val = make(i, j)

        for a in range(i, n):
            for b in range(0, n-2):
                if i==a and j+2>=b:
                    continue

                max_val = max(val+make(a, b), max_val)

print(max_val)