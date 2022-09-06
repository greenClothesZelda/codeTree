n = int(input())

x, y = 0, 0

toward = {
    "N":0,
    "E":1,
    "S":2,
    "W":3
}

dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]
cnt = 0
for i in range(n):
    way, length = tuple(input().split())
    length = int(length)

    for _ in range(length):
        x, y = x+dxs[toward[way]], y+dys[toward[way]]
        cnt+=1
        if x == 0 and y== 0:
            print(cnt)
            exit(0)
print(-1)
