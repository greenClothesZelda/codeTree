input()
arr = list(map(int, input().split()))

cnt = 0

for i in range(len(arr)-2):
    for j in range(i+1, len(arr)):
        a = arr[i+1:j]
        
        for k in a:
            if k>=arr[i] and k<=arr[j]:
                cnt+=1

print(cnt)