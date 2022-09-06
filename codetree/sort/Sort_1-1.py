input()
arr= list(map(int, input().split()))
#print(arr)
arr.sort()
for i in arr:
    print(i, end= " ")
print()
arr = arr[::-1]
for i in arr:
    print(i, end=" ")