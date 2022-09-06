class Person:
    def __init__(self, name, h, w):
        self.name = name
        self.h = h
        self.w = w

n = int(input())
arr= []
for _ in range(n):
    val = input().split()
    arr.append(Person(val[0], int(val[1]), int(val[2])))

arr.sort(key=lambda x: (x.h, -x.w))

for x in arr:
    print(f"{x.name} {x.h} {x.w}")