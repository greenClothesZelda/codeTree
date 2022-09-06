arr = list(map(int, input().split()))

rst = arr[0] - arr[2]
rst *= -60
rst -= arr[1] - arr[3]
print(rst)