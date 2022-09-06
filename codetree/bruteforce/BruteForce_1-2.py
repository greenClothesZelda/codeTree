val = input()

open_arr = []
close_arr = []
cnt = 0
for alpha in val:
    if alpha == '(':
        open_arr.append(cnt)
    else:
        close_arr.append(cnt)
    cnt+=1
cnt = 0

for i in range(len(open_arr)):
    a = open_arr[i]
    while len(close_arr) !=0 and close_arr[0] <= a:
        del close_arr[0]

    cnt+=len(close_arr)
print(cnt)