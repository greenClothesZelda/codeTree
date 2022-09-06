val, n = list(map(int, input().split()))

rst = []

while val !=0:
    rst.append(val%n)
    val//=n

_sum = 0

rst = rst[::-1]

for elem in rst:
    _sum *= 10
    _sum+= elem
print(_sum)