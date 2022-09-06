n = int(input())

arr = [0] * 101

for _ in range(n):
    x, val = input().split()
    x = int(x)

    arr[x] += 1 if val == 'G' else -1

rst = 0
for length in range(len(arr), 0, -1):
    for i in range(len(arr) - length+1):
        sub_list = arr[i:i+length]
        if sub_list[0] == 0 or sub_list[len(sub_list)-1] == 0:
            continue
        if sum(sub_list) == 0:
            rst = length-1
            print(rst)
            exit(0)
print(rst)