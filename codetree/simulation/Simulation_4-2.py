arr = [
    [0]*2001
    for _ in range(2001)
]

def draw(inf):
    for i in range(inf[0], inf[2]):
        for j in range(inf[1], inf[3]):
            if arr[i][j] == 0:
                arr[i][j]+=1


def remove(inf):
    for i in range(inf[0], inf[2]):
        for j in range(inf[1], inf[3]):
            if arr[i][j] == 1:
                arr[i][j]-=1

for _ in range(2):
    _list = list(map(int, input().split()))
    for i in range(4):
        _list[i]+=1000

    draw(_list)
_list = list(map(int, input().split()))
for i in range(4):
    _list[i] += 1000

remove(_list)

rst = 0

for i in arr:
    rst += sum(i)

print(rst)