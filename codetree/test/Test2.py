import math

arr = [2]

n = int(input())

for i in range(3, int(math.sqrt(n))+1, 2):
    for elem in arr:
        rst = False
        if i%elem == 0:
            rst = True
            break
        if not rst:
            arr.append(i)


rst = False
for elem in arr:
    if n % elem == 0:
        rst = True
        break
if not rst:
    print("P")
else:
    print("C")
