arr = [0]*201

n = int(input())

for _ in range(n):
    a, b =list(map(int, input().split()))
    a+=100
    b+=100

    for i in range(a, b):
        arr[i]+=1
_max = 0
for elem in arr:
    if _max<elem:
        _max = elem
print(_max)