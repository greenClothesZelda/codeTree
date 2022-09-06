input()
arr_2d = []
arr_2d.append(
    list(map(int, input().split()))
    for _ in range(2)
)
print(arr_2d)

arr_2d[0].sort()
arr_2d[1].sort()

print("Yes" if arr_2d[0] == arr_2d[1] else "No")