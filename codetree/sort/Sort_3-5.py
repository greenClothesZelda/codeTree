class Person:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

arr = []
for _ in range(5):
    input_val = input().split()
    arr.append(Person(input_val[0], int(input_val[1]), float(input_val[2])))

arr.sort(key=lambda x: x.name)
print("name")
for x in arr:
    print(f"{x.name} {x.height} {x.weight}")
print()

arr.sort(key=lambda x: -x.height)
print("height")
for x in arr:
    print(f"{x.name} {x.height} {x.weight}")
