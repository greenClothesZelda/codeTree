val = input()

cnt = 0

order_dict = {
    "F": 0,
    "L": 3,
    "R": 1
}

way = 0

dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]

x, y = 0, 0

for order in val:
    cnt+=1
    if order == "F":
       x, y = x+dxs[way], y+dys[way]

    way+=order_dict[order]
    way%=4

    if x== 0 and y ==0:

        print(cnt)
        exit(0)
print(-1)