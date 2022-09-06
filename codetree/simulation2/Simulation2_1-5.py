dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

n, m = tuple(map(int, input().split()))

way = 0

arr = [
    [0]*m
    for _ in range(n)
]

def in_range(x,y):
    try:
        return arr[x][y]
    except:
        return 1

x, y = 0, 0

for i in range(n*m):
    arr[x][y] = i+1

    if in_range(x+dxs[way], y+dys[way]) != 0:
        way+=1
        way%=4

    x,y = (x+dxs[way], y+dys[way])

for sub in arr:
    print(*sub)