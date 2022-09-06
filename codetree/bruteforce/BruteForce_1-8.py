import sys

n = int(input())

arr = [
    int(input())
    for _ in range(n)
]

total = sum(arr)

max_val = sys.maxsize

for i in range(n):
    _sum = 0
    a = total

    for elem in arr:
        a -= elem
        _sum += a
    arr.append(arr[0])
    del arr[0]

    max_val = min(max_val, _sum)
print(max_val)