N = int(input())
list = []
for i in range(N):
    list.append(input())
list.sort()
result_str = "\n".join(list)
print(result_str)