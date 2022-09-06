arr = list(map(int, input().split()))

rst = arr[0] - 11
rst *= 24
rst += arr[1] - 11
rst *= 60
rst += arr[2] -11
if(rst<0):
    print(-1)
else:
    print(rst)