n, t = tuple(map(int, input().split()))

dic = {
    "U":2,
    "D":1,
    "R":0,
    "L":3
}

dx, dy = [0, 1, -1, 0], [1, 0, 0, -1]

def in_range(x,y):
    if x<=0 or y<=0:
        return False
    if x>n or y>n:
        return False
    return True

def move(x, y, d):
    if in_range(x+dx[d], y+dy[d]):
        return x+dx[d], y+dy[d], d
    else:
        return x, y, (3 - d)%4

x, y, d = input().split()
d = dic[d]
x = int(x)
y = int(y)

for _ in range(t):
    x, y, d = move(x, y, d)

print(x, y)