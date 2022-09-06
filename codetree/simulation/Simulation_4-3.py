arr = [
    [0]*201
    for _ in range(201)
]

def draw(inf):
    for i in range(inf[0], inf[2]):
        for j in range(inf[1], inf[3]):
            if arr[i][j] == 0:
                arr[i][j]+=1

n = int(input())
for _ in range(n):
    _list = list(map(int, input().split()))
    for i in range(2):
        _list[i]+=100
    _list.append(_list[0]+8)
    _list.append(_list[1] + 8)
    draw(_list)

rst = 0

for i in arr:
    rst += sum(i)

print(rst)