str_arr = [
    input()
    for _ in range(2)
]

str_arr[0] = sorted(str_arr[0])
str_arr[1] = sorted(str_arr[1])

print("Yes" if str_arr[0] == str_arr[1] else "No")