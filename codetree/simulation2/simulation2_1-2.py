way = 0

x, y = 0, 0

val = input()

toward = {
    "L":3,
    "R":1
}


dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

for order in val:
    if order == 'F':
        x, y = x+dx[way%4], y +dy[way%4]
    else:
        way += toward[order]

print(x, y)