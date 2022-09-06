val = input()

rst = 0

for elem in val:
    rst*=2
    rst+=int(elem)
rst*=17

rst = format(rst, 'b')
print(rst)