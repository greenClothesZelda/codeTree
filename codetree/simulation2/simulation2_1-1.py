dir_num = 0
x,y = 0, 0

toward = ['N', 'E', 'S', 'W']

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

n = int(input())

for _ in range(n):
    val = input().split()
    weight = int(val[1])
    x, y  = x+weight*dx[toward.index(val[0])], y+weight*dy[toward.index(val[0])]

print(f"{x} {y}")