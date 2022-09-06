n, m = list(map(int, input().split()))

arr = [
    input().split()
    for _ in range(n)
]

start = arr[0][0]

if arr[len(arr)-1][len(arr[len(arr)-1])-1] == start:
    print(0)
    exit(0)

cnt = 0

for i in range(1,n):
    for j in range(1,m):
        if arr[i][j] == start:
            continue
        for k in range(i+1,n-1):
            a = arr[k][j+1:m-1]
            for elem in a:
                if elem == start:
                    cnt+=1
print(cnt)