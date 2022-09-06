arr = [
    [0]*2001
    for _ in range(2001)
]

for i in range(1, 4):
    val = list(map(int, input().split()))
    for x in range(val[0]+1000, val[2]+1000):
        for y in range(val[1]+1000, val[3]+1000):
            arr[x][y] +=i

cnt = 0

for x in range(len(arr)):
    for y in range(len(arr)):
        if arr[x][y] > 3:
            cnt += 1
print(cnt)