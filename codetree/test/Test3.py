n = int(input())

arr = list(map(int, input().split()))

max_val = 0

for i in range(len(arr)):
    for j in range(i, len(arr)):
        a = arr[j] - arr[i]
        max_val = max(max_val, a)
print(max_val)