import sys

n = int(input())

arr = list(map(int, input().split()))

min_val = sys.maxsize

for i in range(len(arr)):
    _sum = 0
    for j in range(len(arr)):
        _sum += abs(i-j)*arr[j]
    min_val = min(_sum, min_val)
print(min_val)