arr = [
    list(map(int, input().split()))
    for _ in range(19)
]

mid_point = [-1, -1]

def get(x,y):
    if x < 0 or y < 0:
        return -100
    if x >= 19 or y >= 19:
        return -100
    return arr[x][y]

dxs = [0, 1, 1, 1]
dys = [1, 1, 0, -1]

def check(x,y, val):
    global mid_point
    for way in range(len(dys)):
        _sum = 0
        a, b = x, y
        rst = True
        mid_point = [a+2*dxs[way], b+2*dys[way]]
        for _ in range(5):
            if get(a,b) != val:
                rst = False
                break
            a, b = a+dxs[way], b+dys[way]
        if rst:
            return True

    return False

for i in range(19):
    for j in range(19):
        if arr[i][j] == 0:
            continue
        for val in range(2):
            if check(i, j, val+1):
                print(val+1)
                print(mid_point[0]+1, mid_point[1]+1)
                exit(0)
print("0")