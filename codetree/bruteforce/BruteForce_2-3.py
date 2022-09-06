_n = input()

arr = list(map(int, input().split()))

cnt = 0

for i in range(len(arr)):
    for j in range(i, len(arr)):
        a = arr[i:j+1]
        if len(a) == 0:
            continue
        if sum(a)/len(a) in a:

            cnt+=1
print(cnt)