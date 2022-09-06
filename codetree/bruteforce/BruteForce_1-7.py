import copy
import sys


def cal_len(arr):
    sum = 0
    for i in range(1, len(arr)):
        sum+=abs(arr[i][0] - arr[i-1][0])
        sum+=abs(arr[i][1] - arr[i-1][1])
    return sum

point = []

n = int(input())

for _ in range(n):
    point.append(
        tuple(map(int, input().split()))
    )

min_val = sys.maxsize

for i in range(1,len(point)-1):
    clone = copy.deepcopy(point)
    del clone[i]
    min_val = min(cal_len(clone), min_val)
print(min_val)
