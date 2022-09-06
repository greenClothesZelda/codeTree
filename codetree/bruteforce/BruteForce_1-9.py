val = input()

open_arr = []
close_arr = []

for i in range(1,len(val)):
    if val[i] == val[i-1]:
        if val[i] == '(':
            open_arr.append(i)
        else:
            close_arr.append(i)

_sum = 0

for elem in open_arr:
    if len(close_arr) == 0:
        break
    while close_arr[0] < elem:
        del close_arr[0]
        if len(close_arr) == 0:
            break
    _sum += len(close_arr)

print(_sum)