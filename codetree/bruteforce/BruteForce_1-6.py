n = list(input())

change = False

for i in range(len(n)):
    if n[i] == '0':
        n[i] = '1'
        change = True
        break

if not change:
    n[len(n)-1] = '0'

rst = '0b'+"".join(n)

print(int(rst, 2))