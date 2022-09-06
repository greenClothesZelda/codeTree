class Student:
    def __init__(self, input_val):
        self.input_val = input_val
        input_val[2] *=-1


n = int(input())
cnt= 1
arr = []
for _ in range(n):
    input_val = list(map(int,input().split()))
    input_val.append(cnt)
    arr.append(Student(input_val))
    cnt+=1

arr.sort(key=lambda x: x.input_val)
arr = arr[::-1]

for i in arr:
    i.input_val[2] *= -1
    print(*i.input_val)