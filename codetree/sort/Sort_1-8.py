n, k, t = tuple(input().split())
n = int(n)
k = int(k)

arr = []
for _ in range(n):
    a = input()
    if t == a[:len(t)]:
        arr.append(a)

arr.sort()

print(arr[k-1])