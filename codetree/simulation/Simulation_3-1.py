n, k = list(map(int, input().split()))
arr = [0]*(n+1)

for _ in range(k):
    a, b =list(map(int, input().split()))
    for i in range(a, b+1):
        arr[i]+=1
_max = 0
for elem in arr:
    if _max<elem:
        _max = elem
print(_max)