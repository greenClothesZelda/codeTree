class Person:
    def __init__(self, name= "n", num = 0, region = "n"):
        self.name = name
        self.num = num
        self.region = region

n = int(input())

arr = []

for _ in range(n):
    arr.append(Person(*tuple(input().split())))

arr.sort(key=lambda x: x.name)
person = arr[len(arr)-1]


print(f"name {person.name}")
print(f"addr {person.num}")
print(f"city {person.region}")
