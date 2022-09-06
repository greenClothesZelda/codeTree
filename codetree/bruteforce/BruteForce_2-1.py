import sys

n, m  = tuple(map(int, input().split()))

arr = list(map(int, input().split()))

max_val = -sys.maxsize

for i in range(n-m+1):
    a = arr[i:i+m]
    _sum = 0
    for elem in a:
        _sum +=elem
    max_val = max(max_val, _sum)
print(max_val)