n = int(input())

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

def get(x,y):
    try:
        return arr[x][y]
    except:
        return 0
max_val = 0
for i in range(len(arr)):
    for j in range(len(arr[i])-2):
        x = get(i,j)+get(i,j+1)+get(i,j+2)
        max_val = max(max_val, x)
print(max_val)