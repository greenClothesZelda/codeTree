class Student:
    def __init__(self, value):
        self.name = value[0]
        self.tall = int(value[1])
        self.weight = int(value[2])

N = int(input())

students = [
    Student(tuple(input().split()))
    for _ in range(N)
]
students.sort(key=lambda x:x.tall)

for stu in students:
    print(f"{stu.name} {stu.tall} {stu.weight}")