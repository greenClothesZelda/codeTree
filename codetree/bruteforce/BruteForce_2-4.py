import copy

n, m = tuple(map(int, input().split()))

arr = list(map(int, input().split()))
brr = list(map(int, input().split()))

check_list = []

cnt = 0

brr.sort()

for i in range(n-m+1):
    sub_list = arr[i:i+m]
    if brr == sorted(sub_list):
        cnt+=1
        check_list.append(sub_list)
print(cnt)
