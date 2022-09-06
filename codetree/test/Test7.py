dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]
way = 0

arr = []

n = int(input())

for _ in range(n):
    val = input()
    sub_arr = []
    for elem in val:
        sub_arr.append(1 if elem == '/' else 2)
    arr.append(sub_arr)

k = int(input())

x, y = 0, 0

def check(x, y):
    if x < 0 or y < 0:
        return 0
    try:
        return arr[x][y]
    except:
        return 0

for _ in range(k-1):
    if check(x+dxs[way], y + dys[way]) == 0:
        way = (way+1)%4
    else:
        x, y = x+dxs[way], y + dys[way]

way = (way+1)%4

cnt = 0


while not (check(x,y) == 0):
    right = True

    if way%2 == 0:
        right = not right

    way += 1 if right else -1

    way %= 4

    if not(arr[x][y] == 1):
        way = (way+2)%4

    x, y = x+dxs[way], y+dys[way]

    cnt += 1

print(cnt)





