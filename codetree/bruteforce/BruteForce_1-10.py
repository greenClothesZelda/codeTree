import sys

n = int(input())
arr = list(map(int, input().split()))

max_val = -sys.maxsize

for i in range(len(arr)):
    a = arr[i]
    for j in range(len(arr)):
        if abs(i-j) <= 1:
            continue
        max_val = max(max_val, a+arr[j])
print(max_val)