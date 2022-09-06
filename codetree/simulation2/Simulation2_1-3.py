n = int(input())

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

def get(x, y):
    if x<0 or y<0:
        return 0
    if x>=n or y>=n:
        return 0
    return arr[x][y]

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

rst = 0


for i in range(n):
    for j in range(n):
        cnt = 0
        for dx, dy in zip(dxs, dys):
            if get(i+dx, j+dy) == 1:
                #print(i+dx,j+dy)
                cnt+=1
        if cnt >= 3:
            # print(i, j)
            rst+=1

print(rst)
