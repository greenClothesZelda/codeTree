n, k = list(map(int, input().split()))

arr = [0] * 101

for _ in range(n):
    num, x = list(map(int, input().split()))
    arr[x]+=num

max_val = 0

if len(arr)-2*k<=0:
    max_val = sum(arr)

for i in range(len(arr)-2*k):
    sub_list = arr[i:i+2*k+1]

    max_val = max(sum(sub_list), max_val)
print(max_val)