input()
arr = [
    list(map(int, input().split()))
    for _ in range(2)
]

arr[0].sort()
arr[1].sort()

print("Yes" if arr[0] == arr[1] else "No")