n = int(input())
arr = list(map(int, input().split()))
arr.sort()

max_val = 0

for _ in range(n):
    a = 0
    a += arr[0]
    del arr[0]
    a += arr.pop()
    if a >max_val:
        max_val = a
print(max_val)