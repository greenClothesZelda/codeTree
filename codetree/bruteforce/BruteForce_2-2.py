n, k = tuple(map(int, input().split()))

arr = []

def add(index, val):
    while index >= len(arr):
        arr.append("N")
    arr[index] = val
    return


for _ in range(n):
    index, point = input().split()
    add(int(index), point)

max_val = 0

if len(arr)-k<=0:
    for elem in arr:
        max_val+= 2 if elem == "H" else 1 if elem == "G" else 0

for i in range(len(arr)-k):
    _sum = 0
    #print(arr[i:i+k+1])
    for elem in arr[i:i+k+1]:
        _sum+= 2 if elem == "H" else 1 if elem == "G" else 0
    max_val = max(max_val, _sum)
print(max_val)